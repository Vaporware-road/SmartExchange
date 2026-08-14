"""
Telegram service for sending messages and media to Telegram channels.
Compatible with python-telegram-bot v20 (async).
"""
import asyncio
import concurrent.futures
import logging
from typing import Any, Iterable, List, Mapping, Optional

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import TelegramError, BadRequest, TimedOut, NetworkError

logger = logging.getLogger(__name__)


def _run_coroutine_sync(make_coroutine):
    """Run an async send from sync code (Celery task, DRF view, management command).

    ``make_coroutine`` is a zero-arg callable returning a fresh coroutine, not a
    coroutine object: the coroutine is only created on the branch that awaits it, so
    no "coroutine was never awaited" warning is possible.

    The loop probe is deliberately isolated from running the coroutine. The previous
    version wrapped both in one ``try/except RuntimeError``, so a RuntimeError raised
    *inside* an already-executing send fell into the handler and ran the whole send a
    second time — publishing the same price message/photo to the channel twice.
    """
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop_is_running = False
    else:
        loop_is_running = True

    if loop_is_running:
        # Already inside an event loop (e.g. an async caller): asyncio.run() would
        # raise here, so hand the work to a thread that owns its own loop.
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            return executor.submit(lambda: asyncio.run(make_coroutine())).result()

    return asyncio.run(make_coroutine())

# Import logging utility (with try-except to avoid circular imports)
try:
    from setting.utils import log_telegram_event
except ImportError:
    log_telegram_event = None


class TelegramService:
    """Service class for interacting with Telegram Bot API."""
    
    def __init__(self, token):
        """
        Initialize Telegram service with bot token.
        
        Args:
            token: Telegram bot token from @BotFather
        """
        if not token:
            raise ValueError("Bot token is required")
        self.token = token
        self.bot = Bot(token=token)

    @staticmethod
    def _build_inline_keyboard(buttons: Optional[Iterable[Iterable[Mapping[str, Any]]]]):
        if not buttons:
            return None

        keyboard: List[List[InlineKeyboardButton]] = []
        for row in buttons:
            button_row: List[InlineKeyboardButton] = []
            for button in row:
                text = button.get("text")
                if not text:
                    continue
                kwargs = {}
                if "url" in button:
                    kwargs["url"] = button["url"]
                elif "callback_data" in button:
                    kwargs["callback_data"] = button["callback_data"]
                elif "switch_inline_query" in button:
                    kwargs["switch_inline_query"] = button["switch_inline_query"]
                elif "switch_inline_query_current_chat" in button:
                    kwargs["switch_inline_query_current_chat"] = button[
                        "switch_inline_query_current_chat"
                    ]

                if not kwargs:
                    continue

                button_row.append(InlineKeyboardButton(text=text, **kwargs))
            if button_row:
                keyboard.append(button_row)

        if not keyboard:
            return None

        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    async def _send_message_async(
        self,
        chat_id,
        text,
        parse_mode="HTML",
        buttons=None,
    ):
        """
        Async helper method to send a message.
        
        Args:
            chat_id: Telegram chat ID (can be channel username or ID)
            text: Message text to send
            parse_mode: Message parse mode (HTML, Markdown, or None)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        if not chat_id:
            return False, "Chat ID is required"
        
        if not text or not text.strip():
            return False, "Message text cannot be empty"
        
        try:
            reply_markup = self._build_inline_keyboard(buttons)
            await self.bot.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode=parse_mode,
                reply_markup=reply_markup,
            )
            logger.info(f"Message sent successfully to {chat_id}")
            # Log to database
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='INFO',
                        message='Message sent to Telegram channel',
                        details={
                            'event': 'send_message',
                            'chat_id': str(chat_id),
                            'text_length': len(text),
                            'parse_mode': parse_mode,
                            'has_buttons': bool(buttons),
                        },
                    )
                except Exception:
                    pass  # Don't fail if logging fails
            return True, "Message sent successfully."
        except BadRequest as e:
            error_msg = f"Bad request: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Failed to send message to Telegram',
                        details={
                            'event': 'send_message_bad_request',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except TimedOut as e:
            error_msg = f"Request timed out: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram request timed out',
                        details={
                            'event': 'send_message_timeout',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except NetworkError as e:
            error_msg = f"Network error: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram network error',
                        details={
                            'event': 'send_message_network_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except TelegramError as e:
            error_msg = f"Telegram error: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram API error',
                        details={
                            'event': 'send_message_telegram_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.exception(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='CRITICAL',
                        message='Unexpected error sending Telegram message',
                        details={
                            'event': 'send_message_unexpected_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg

    def send_message(self, chat_id, text, parse_mode="HTML", buttons=None):
        """
        Send a text message to a Telegram chat.
        This is a synchronous wrapper for the async method.
        
        Args:
            chat_id: Telegram chat ID (can be channel username or ID)
            text: Message text to send
            parse_mode: Message parse mode (HTML, Markdown, or None)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        return _run_coroutine_sync(
            lambda: self._send_message_async(chat_id, text, parse_mode, buttons)
        )

    async def _send_photo_async(
        self,
        chat_id,
        photo,
        caption=None,
        parse_mode="HTML",
        buttons=None,
    ):
        """
        Async helper method to send a photo.
        
        Args:
            chat_id: Telegram chat ID (can be channel username or ID)
            photo: Photo file (file path, file-like object, or file_id)
            caption: Optional photo caption
            parse_mode: Caption parse mode (HTML, Markdown, or None)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        if not chat_id:
            return False, "Chat ID is required"
        
        if not photo:
            return False, "Photo is required"
        
        try:
            reply_markup = self._build_inline_keyboard(buttons)
            await self.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                parse_mode=parse_mode if caption else None,
                reply_markup=reply_markup,
            )
            logger.info(f"Photo sent successfully to {chat_id}")
            # Log to database
            if log_telegram_event:
                try:
                    cap_preview = (caption[:100] + '…') if caption and len(caption) > 100 else caption
                    log_telegram_event(
                        level='INFO',
                        message='Photo sent to Telegram channel',
                        details={
                            'event': 'send_photo',
                            'chat_id': str(chat_id),
                            'caption_length': len(caption) if caption else 0,
                            'caption_preview': cap_preview or None,
                            'has_buttons': bool(buttons),
                        },
                    )
                except Exception:
                    pass  # Don't fail if logging fails
            return True, "Photo sent successfully."
        except BadRequest as e:
            error_msg = f"Bad request: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Failed to send photo to Telegram',
                        details={
                            'event': 'send_photo_bad_request',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except TimedOut as e:
            error_msg = f"Request timed out: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram photo request timed out',
                        details={
                            'event': 'send_photo_timeout',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except NetworkError as e:
            error_msg = f"Network error: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram network error (photo)',
                        details={
                            'event': 'send_photo_network_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except TelegramError as e:
            error_msg = f"Telegram error: {str(e)}"
            logger.error(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='ERROR',
                        message='Telegram API error (photo)',
                        details={
                            'event': 'send_photo_telegram_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.exception(error_msg)
            if log_telegram_event:
                try:
                    log_telegram_event(
                        level='CRITICAL',
                        message='Unexpected error sending Telegram photo',
                        details={
                            'event': 'send_photo_unexpected_error',
                            'chat_id': str(chat_id),
                            'error': error_msg,
                        },
                    )
                except Exception:
                    pass
            return False, error_msg

    def send_photo(self, chat_id, photo, caption=None, parse_mode="HTML", buttons=None):
        """
        Send a photo to a Telegram chat.
        This is a synchronous wrapper for the async method.
        
        Args:
            chat_id: Telegram chat ID (can be channel username or ID)
            photo: Photo file (file path, file-like object, or file_id)
            caption: Optional photo caption
            parse_mode: Caption parse mode (HTML, Markdown, or None)
        
        Returns:
            tuple: (success: bool, message: str)
        """
        return _run_coroutine_sync(
            lambda: self._send_photo_async(chat_id, photo, caption, parse_mode, buttons)
        )
