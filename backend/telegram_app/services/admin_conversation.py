"""In-bot admin panel (reply keyboards) for staff Telegram IDs."""

from __future__ import annotations

from django.db.models import Count
from django.utils import timezone

from ..models import (
    BotSession,
    CustomerProfile,
    ExchangeRequest,
    ReengageCampaign,
    ReengageOffer,
)
from .analytics_service import (
    format_analytics_dashboard_summary,
    format_customer_analysis,
    format_exchange_requests,
    format_new_members,
)
from .customer_tags import (
    AdminTagImmutable,
    customers_ranked_for_bot,
    display_name,
    effective_tag,
    set_customer_tag,
)
from .exchange_ops import hold_request, set_request_status
from .reengage_service import schedule_next_run, send_to_audience
from .staff_access import is_bot_admin

CB_ADMIN_HOME = "admin:home"
CB_ADMIN_PENDING = "admin:pending"
CB_ADMIN_RECENT = "admin:recent"
CB_ADMIN_STATS = "admin:stats"
CB_ADMIN_CLOSE = "admin:close"
CB_ADMIN_TAG = "admin:tag"
CB_ADMIN_BACK_LIST = "admin:back_list"
CB_ADMIN_BACK_DETAIL = "admin:back_detail"
CB_ADMIN_OPEN_PREFIX = "admin:open:"
CB_ADMIN_TAG_PREFIX = "admin:settag:"
CB_ADMIN_TAG_USER_PREFIX = "admin:taguser:"
CB_ADMIN_CHANGE_STATE = "admin:change_state"
CB_ADMIN_HOLD = "admin:hold"
CB_ADMIN_STATE_PREFIX = "admin:state:"
CB_ADMIN_ANALYTICS = "admin:analytics"
CB_ADMIN_CUSTOMER_ANALYSIS = "admin:customer_analysis"
CB_ADMIN_REENGAGE = "admin:reengage"
CB_ADMIN_ANALYTICS_EXCHANGE = "admin:analytics_exchange"
CB_ADMIN_ANALYTICS_MEMBERS = "admin:analytics_members"
CB_ADMIN_EXCH_SUCCESS = "admin:exch_success"
CB_ADMIN_EXCH_PENDING = "admin:exch_pending"
CB_ADMIN_MEMBERS_1 = "admin:members:1"
CB_ADMIN_MEMBERS_3 = "admin:members:3"
CB_ADMIN_MEMBERS_9 = "admin:members:9"
CB_ADMIN_MEMBERS_12 = "admin:members:12"
CB_ADMIN_REENGAGE_SEND = "admin:reengage_send"
CB_ADMIN_REENGAGE_PERIODIC = "admin:reengage_periodic"
CB_ADMIN_REENGAGE_OFFER = "admin:reengage_offer"
CB_ADMIN_AUDIENCE_PREFIX = "admin:audience:"
CB_ADMIN_SCHEDULE_PREFIX = "admin:schedule:"
CB_ADMIN_REENGAGE_CONFIRM = "admin:reengage_confirm"
CB_ADMIN_OFFER_SAVE = "admin:offer_save"

BTN_ADMIN_PENDING = "Pending requests"
BTN_ADMIN_RECENT = "Recent requests"
BTN_ADMIN_STATS = "Bot stats"
BTN_ADMIN_HOME = "Admin menu"
BTN_ADMIN_TAG = "Set customer tag"
BTN_ADMIN_BACK_LIST = "Back to list"
BTN_ADMIN_BACK_DETAIL = "Back"
BTN_ADMIN_CHANGE_STATE = "Change state"
BTN_ADMIN_HOLD = "Confirm (Hold the request)"
BTN_STATE_NEW = "New"
BTN_STATE_CANCELLED = "Canceled"
BTN_STATE_SUCCESSFUL = "Successful"
BTN_ADMIN_ANALYTICS = "Analytics Dashboard"
BTN_ADMIN_CUSTOMER_ANALYSIS = "Customer Analysis"
BTN_ADMIN_REENGAGE = "Re-engagement"
BTN_ADMIN_EXCHANGE_REQUESTS = "Exchange Requests"
BTN_ADMIN_NEW_MEMBERS = "New members"
BTN_ADMIN_EXCH_SUCCESS = "Successful Requests"
BTN_ADMIN_EXCH_PENDING = "Pending Requests"
BTN_ADMIN_MEMBERS_1 = "Last month"
BTN_ADMIN_MEMBERS_3 = "Last 3 months"
BTN_ADMIN_MEMBERS_9 = "Last 9 months"
BTN_ADMIN_MEMBERS_12 = "Last year"
BTN_ADMIN_BACK_ANALYTICS = "Back to Analytics"
BTN_ADMIN_REENGAGE_SEND = "Send now"
BTN_ADMIN_REENGAGE_PERIODIC = "Periodic Campaigns"
BTN_ADMIN_REENGAGE_OFFER = "Offer Creation"
BTN_ADMIN_AUD_GLOBAL = "Audience: Global"
BTN_ADMIN_AUD_VIP = "Audience: VIP"
BTN_ADMIN_AUD_SPECIAL = "Audience: Special currencies"
BTN_ADMIN_AUD_INACTIVE = "Audience: Inactive"
BTN_ADMIN_SCHED_DAILY = "Schedule: Daily"
BTN_ADMIN_SCHED_WEEKLY = "Schedule: Weekly"
BTN_ADMIN_SCHED_MONTHLY = "Schedule: Monthly"
BTN_ADMIN_CONFIRM_SAVE = "Confirm & save"
BTN_ADMIN_OFFER_SAVE = "Save offer"
BTN_TAG_GLOBAL = "Tag: Global"
BTN_TAG_VIP = "Tag: VIP"
BTN_TAG_SPECIAL = "Tag: Special"

TAG_USER_PAGE_SIZE = 8

ADMIN_LABEL_TO_CB: dict[str, str] = {
    BTN_ADMIN_PENDING: CB_ADMIN_PENDING,
    BTN_ADMIN_RECENT: CB_ADMIN_RECENT,
    BTN_ADMIN_STATS: CB_ADMIN_STATS,
    BTN_ADMIN_HOME: CB_ADMIN_HOME,
    BTN_ADMIN_TAG: CB_ADMIN_TAG,
    BTN_ADMIN_BACK_LIST: CB_ADMIN_BACK_LIST,
    BTN_ADMIN_BACK_DETAIL: CB_ADMIN_BACK_DETAIL,
    BTN_ADMIN_CHANGE_STATE: CB_ADMIN_CHANGE_STATE,
    BTN_ADMIN_HOLD: CB_ADMIN_HOLD,
    BTN_STATE_NEW: f"{CB_ADMIN_STATE_PREFIX}new",
    BTN_STATE_CANCELLED: f"{CB_ADMIN_STATE_PREFIX}cancelled",
    BTN_STATE_SUCCESSFUL: f"{CB_ADMIN_STATE_PREFIX}successful",
    BTN_ADMIN_ANALYTICS: CB_ADMIN_ANALYTICS,
    BTN_ADMIN_CUSTOMER_ANALYSIS: CB_ADMIN_CUSTOMER_ANALYSIS,
    BTN_ADMIN_REENGAGE: CB_ADMIN_REENGAGE,
    BTN_ADMIN_EXCHANGE_REQUESTS: CB_ADMIN_ANALYTICS_EXCHANGE,
    BTN_ADMIN_NEW_MEMBERS: CB_ADMIN_ANALYTICS_MEMBERS,
    BTN_ADMIN_EXCH_SUCCESS: CB_ADMIN_EXCH_SUCCESS,
    BTN_ADMIN_EXCH_PENDING: CB_ADMIN_EXCH_PENDING,
    BTN_ADMIN_MEMBERS_1: CB_ADMIN_MEMBERS_1,
    BTN_ADMIN_MEMBERS_3: CB_ADMIN_MEMBERS_3,
    BTN_ADMIN_MEMBERS_9: CB_ADMIN_MEMBERS_9,
    BTN_ADMIN_MEMBERS_12: CB_ADMIN_MEMBERS_12,
    BTN_ADMIN_BACK_ANALYTICS: CB_ADMIN_ANALYTICS,
    BTN_ADMIN_REENGAGE_SEND: CB_ADMIN_REENGAGE_SEND,
    BTN_ADMIN_REENGAGE_PERIODIC: CB_ADMIN_REENGAGE_PERIODIC,
    BTN_ADMIN_REENGAGE_OFFER: CB_ADMIN_REENGAGE_OFFER,
    BTN_ADMIN_AUD_GLOBAL: f"{CB_ADMIN_AUDIENCE_PREFIX}global",
    BTN_ADMIN_AUD_VIP: f"{CB_ADMIN_AUDIENCE_PREFIX}vip",
    BTN_ADMIN_AUD_SPECIAL: f"{CB_ADMIN_AUDIENCE_PREFIX}special",
    BTN_ADMIN_AUD_INACTIVE: f"{CB_ADMIN_AUDIENCE_PREFIX}inactive",
    BTN_ADMIN_SCHED_DAILY: f"{CB_ADMIN_SCHEDULE_PREFIX}daily",
    BTN_ADMIN_SCHED_WEEKLY: f"{CB_ADMIN_SCHEDULE_PREFIX}weekly",
    BTN_ADMIN_SCHED_MONTHLY: f"{CB_ADMIN_SCHEDULE_PREFIX}monthly",
    BTN_ADMIN_CONFIRM_SAVE: CB_ADMIN_REENGAGE_CONFIRM,
    BTN_ADMIN_OFFER_SAVE: CB_ADMIN_OFFER_SAVE,
    BTN_TAG_GLOBAL: f"{CB_ADMIN_TAG_PREFIX}global",
    BTN_TAG_VIP: f"{CB_ADMIN_TAG_PREFIX}vip",
    BTN_TAG_SPECIAL: f"{CB_ADMIN_TAG_PREFIX}special",
}

ADMIN_MENU_BUTTONS = [
    [{"text": BTN_ADMIN_PENDING}],
    [{"text": BTN_ADMIN_RECENT}],
    [{"text": BTN_ADMIN_ANALYTICS}],
    [{"text": BTN_ADMIN_CUSTOMER_ANALYSIS}],
    [{"text": BTN_ADMIN_REENGAGE}],
    [{"text": BTN_ADMIN_STATS}],
]

ANALYTICS_MENU_BUTTONS = [
    [{"text": BTN_ADMIN_EXCHANGE_REQUESTS}],
    [{"text": BTN_ADMIN_NEW_MEMBERS}],
    [{"text": BTN_ADMIN_HOME}],
]

EXCHANGE_MENU_BUTTONS = [
    [{"text": BTN_ADMIN_EXCH_SUCCESS}],
    [{"text": BTN_ADMIN_EXCH_PENDING}],
    [{"text": BTN_ADMIN_BACK_ANALYTICS}],
    [{"text": BTN_ADMIN_HOME}],
]

MEMBERS_MENU_BUTTONS = [
    [{"text": BTN_ADMIN_MEMBERS_1}],
    [{"text": BTN_ADMIN_MEMBERS_3}],
    [{"text": BTN_ADMIN_MEMBERS_9}],
    [{"text": BTN_ADMIN_MEMBERS_12}],
    [{"text": BTN_ADMIN_BACK_ANALYTICS}],
    [{"text": BTN_ADMIN_HOME}],
]

REENGAGE_MENU_BUTTONS = [
    [{"text": BTN_ADMIN_AUD_GLOBAL}],
    [{"text": BTN_ADMIN_AUD_VIP}],
    [{"text": BTN_ADMIN_AUD_SPECIAL}],
    [{"text": BTN_ADMIN_AUD_INACTIVE}],
    [{"text": BTN_ADMIN_REENGAGE_PERIODIC}],
    [{"text": BTN_ADMIN_REENGAGE_OFFER}],
    [{"text": BTN_ADMIN_HOME}],
]

AUDIENCE_BUTTONS = [
    [{"text": BTN_ADMIN_AUD_GLOBAL}],
    [{"text": BTN_ADMIN_AUD_VIP}],
    [{"text": BTN_ADMIN_AUD_SPECIAL}],
    [{"text": BTN_ADMIN_AUD_INACTIVE}],
    [{"text": BTN_ADMIN_HOME}],
]

SCHEDULE_BUTTONS = [
    [{"text": BTN_ADMIN_SCHED_DAILY}],
    [{"text": BTN_ADMIN_SCHED_WEEKLY}],
    [{"text": BTN_ADMIN_SCHED_MONTHLY}],
    [{"text": BTN_ADMIN_HOME}],
]

CUSTOMER_ANALYSIS_BUTTONS = [
    [{"text": BTN_ADMIN_TAG}],
    [{"text": BTN_ADMIN_HOME}],
]

ADMIN_MENU_TEXT = (
    "Admin panel\n\n"
    "You are recognized by your Telegram ID (no login).\n"
    "Choose an option:"
)

LIVE_STATUSES = (ExchangeRequest.Status.NEW,)

TAG_PROMPT = "Write any userid or chose from the list:"


def _btn(*labels: str) -> list[list[dict[str, str]]]:
    rows = [[{"text": label}] for label in labels if label != BTN_ADMIN_HOME]
    rows.append([{"text": BTN_ADMIN_HOME}])
    return rows


def _reply(text: str, *, buttons=None) -> dict:
    return {
        "text": text,
        "buttons": buttons,
        "keyboard": "reply",
        "remove_keyboard": False,
        "edit_previous": False,
        "message_id": None,
    }


def _persist(session: BotSession, *, fields: list[str]) -> None:
    update = list(dict.fromkeys(fields + ["last_activity", "updated_at"]))
    session.save(update_fields=update)


def _ctx(session: BotSession) -> dict:
    return dict(session.context or {})


def _set_ctx(session: BotSession, ctx: dict) -> None:
    session.context = ctx


def resolve_admin_label(text: str | None) -> str | None:
    label = (text or "").strip()
    if not label:
        return None
    if label in ADMIN_LABEL_TO_CB:
        return ADMIN_LABEL_TO_CB[label]
    if label.startswith("Req #"):
        try:
            req_id = int(label.split("#", 1)[1].strip().split()[0])
            return f"{CB_ADMIN_OPEN_PREFIX}{req_id}"
        except (IndexError, ValueError):
            return None
    if label.startswith("User "):
        try:
            tid = int(label.split()[1])
            return f"{CB_ADMIN_TAG_USER_PREFIX}{tid}"
        except (IndexError, ValueError):
            return None
    return None


def staff_for_session(session: BotSession):
    return is_bot_admin(session.telegram_user_id, session.bot)


def go_admin_menu(session: BotSession) -> dict:
    staff = staff_for_session(session)
    if staff is None:
        return None
    ctx = _ctx(session)
    for key in (
        "admin_request_id",
        "admin_list_kind",
        "admin_tag_telegram_id",
        "tag_page",
        "reengage_mode",
        "reengage_audience",
        "reengage_message",
        "reengage_schedule",
        "offer_title",
        "offer_body",
    ):
        ctx.pop(key, None)
    _set_ctx(session, ctx)
    session.state = BotSession.State.ADMIN_MENU
    _persist(session, fields=["state", "context"])
    return _reply(ADMIN_MENU_TEXT, buttons=ADMIN_MENU_BUTTONS)


def _format_request_line(req: ExchangeRequest) -> str:
    who = (
        req.customer.username
        or req.customer.first_name
        or str(req.customer.telegram_user_id)
    )
    return (
        f"Req #{req.pk} {req.source_currency}→{req.target_currency} "
        f"{req.amount} [{req.status}] {who}"
    )


def _request_qs(session: BotSession):
    return (
        ExchangeRequest.objects.filter(bot=session.bot)
        .select_related("customer")
        .order_by("-created_at")
    )


def _show_request_list(session: BotSession, *, kind: str) -> dict:
    qs = _request_qs(session)
    if kind == "pending":
        qs = qs.filter(status__in=LIVE_STATUSES)
        title = "Pending requests (New)"
    else:
        title = "Recent requests (last 10)"
        qs = qs[:10]

    rows = list(qs[:10])
    ctx = _ctx(session)
    ctx["admin_list_kind"] = kind
    ctx.pop("admin_request_id", None)
    _set_ctx(session, ctx)
    session.state = BotSession.State.ADMIN_REQUEST_LIST
    _persist(session, fields=["state", "context"])

    if not rows:
        return _reply(
            f"{title}\n\nNo requests found.",
            buttons=_btn(),
        )

    lines = [title, ""] + [_format_request_line(r) for r in rows]
    lines.append("\nTap a request button to open it.")
    buttons = [
        [{"text": f"Req #{r.pk} {r.source_currency}→{r.target_currency}"}]
        for r in rows
    ]
    buttons.append([{"text": BTN_ADMIN_HOME}])
    return _reply("\n".join(lines), buttons=buttons)


def _show_request_detail(session: BotSession, req: ExchangeRequest) -> dict:
    ctx = _ctx(session)
    ctx["admin_request_id"] = req.pk
    _set_ctx(session, ctx)
    session.state = BotSession.State.ADMIN_REQUEST_DETAIL
    _persist(session, fields=["state", "context"])

    customer = req.customer
    who = customer.username or customer.first_name or str(customer.telegram_user_id)
    price = str(req.price_at_request) if req.price_at_request is not None else "N/A"
    text = (
        f"Request #{req.pk}\n"
        f"Status: {req.get_status_display()}\n"
        f"Customer: {who} (tg:{customer.telegram_user_id})\n"
        f"Tag: {effective_tag(customer)}\n"
        f"Pair: {req.source_currency} → {req.target_currency}\n"
        f"Amount: {req.amount}\n"
        f"Price: {price}\n"
        f"TTL: {req.ttl_minutes} min\n"
        f"Created: {req.created_at}"
    )
    buttons = _btn(
        BTN_ADMIN_CHANGE_STATE,
        BTN_ADMIN_HOLD,
        BTN_ADMIN_BACK_LIST,
    )
    return _reply(text, buttons=buttons)


def _show_change_state(session: BotSession) -> dict:
    req = _load_admin_request(session)
    if req is None:
        return go_admin_menu(session)
    session.state = BotSession.State.ADMIN_CHANGE_STATE
    _persist(session, fields=["state"])
    return _reply(
        f"Request #{req.pk} current state: {req.get_status_display()}\n\n"
        "Choose a state:",
        buttons=_btn(
            BTN_STATE_NEW,
            BTN_STATE_CANCELLED,
            BTN_STATE_SUCCESSFUL,
            BTN_ADMIN_BACK_DETAIL,
        ),
    )


def _show_stats(session: BotSession) -> dict:
    qs = ExchangeRequest.objects.filter(bot=session.bot)
    counts = {
        row["status"]: row["n"]
        for row in qs.values("status").annotate(n=Count("id"))
    }
    customers = (
        BotSession.objects.filter(bot=session.bot)
        .values("telegram_user_id")
        .distinct()
        .count()
    )
    text = (
        f"Bot stats — {session.bot.name}\n\n"
        f"Customers (sessions): {customers}\n"
        f"New: {counts.get(ExchangeRequest.Status.NEW, 0)}\n"
        f"Canceled: {counts.get(ExchangeRequest.Status.CANCELLED, 0)}\n"
        f"Successful: {counts.get(ExchangeRequest.Status.SUCCESSFUL, 0)}"
    )
    session.state = BotSession.State.ADMIN_MENU
    _persist(session, fields=["state"])
    return _reply(text, buttons=ADMIN_MENU_BUTTONS)


def _show_analytics(session: BotSession) -> dict:
    session.state = BotSession.State.ADMIN_ANALYTICS
    _persist(session, fields=["state"])
    text = format_analytics_dashboard_summary(session.bot)
    return _reply(text, buttons=ANALYTICS_MENU_BUTTONS)


def _show_customer_analysis(session: BotSession) -> dict:
    session.state = BotSession.State.ADMIN_ANALYTICS
    _persist(session, fields=["state"])
    text = format_customer_analysis(session.bot)
    return _reply(text, buttons=CUSTOMER_ANALYSIS_BUTTONS)


def _show_reengage_menu(session: BotSession) -> dict:
    session.state = BotSession.State.ADMIN_REENGAGE
    _persist(session, fields=["state"])
    return _reply(
        "Re-engagement\n\n"
        "Choose an audience for a one-shot send, or set up periodic campaigns / offers.",
        buttons=REENGAGE_MENU_BUTTONS,
    )


def _load_admin_request(session: BotSession) -> ExchangeRequest | None:
    ctx = _ctx(session)
    req_id = ctx.get("admin_request_id")
    if not req_id:
        return None
    try:
        return (
            ExchangeRequest.objects.select_related("customer")
            .filter(pk=int(req_id), bot=session.bot)
            .first()
        )
    except (TypeError, ValueError):
        return None


def _tag_user_label(profile: CustomerProfile) -> str:
    name = display_name(profile) or "—"
    return f"User {profile.telegram_user_id} {name}"


def _show_tag_user_list(session: BotSession) -> dict:
    ctx = _ctx(session)
    page = int(ctx.get("tag_page") or 0)
    qs = list(customers_ranked_for_bot(session.bot)[:80])
    start = page * TAG_USER_PAGE_SIZE
    chunk = qs[start : start + TAG_USER_PAGE_SIZE]
    ctx.pop("admin_tag_telegram_id", None)
    ctx["tag_page"] = page
    _set_ctx(session, ctx)
    session.state = BotSession.State.ADMIN_SET_TAG
    _persist(session, fields=["state", "context"])

    lines = [
        "Set customer tag",
        "",
        TAG_PROMPT,
        "",
    ]
    if not chunk:
        lines.append("No logged-in customers yet.")
        return _reply("\n".join(lines), buttons=_btn())

    for profile in chunk:
        name = display_name(profile) or "—"
        lines.append(
            f"{profile.telegram_user_id}  {name}  "
            f"tag={effective_tag(profile)}  requests={profile.request_count}"
        )
    buttons = [[{"text": _tag_user_label(p)}] for p in chunk]
    nav = []
    if page > 0:
        nav.append({"text": "◀ Prev"})
    if start + TAG_USER_PAGE_SIZE < len(qs):
        nav.append({"text": "Next ▶"})
    if nav:
        buttons.append(nav)
    buttons.append([{"text": BTN_ADMIN_HOME}])
    return _reply("\n".join(lines), buttons=buttons)


def _show_tag_choices(session: BotSession, profile: CustomerProfile) -> dict:
    if effective_tag(profile) == "admin":
        return _reply(
            f"User {profile.telegram_user_id} is Admin.\n"
            "That tag is not changeable.",
            buttons=_btn(BTN_ADMIN_TAG),
        )
    ctx = _ctx(session)
    ctx["admin_tag_telegram_id"] = profile.telegram_user_id
    _set_ctx(session, ctx)
    session.state = BotSession.State.ADMIN_SET_TAG
    _persist(session, fields=["state", "context"])
    name = display_name(profile) or "—"
    return _reply(
        f"User {profile.telegram_user_id} {name}\n"
        f"Current tag: {effective_tag(profile)}\n\n"
        "Choose a tag:",
        buttons=_btn(BTN_TAG_GLOBAL, BTN_TAG_VIP, BTN_TAG_SPECIAL),
    )


def _handle_reengage_text(session: BotSession, text: str) -> dict | None:
    ctx = _ctx(session)
    mode = ctx.get("reengage_mode")
    stripped = (text or "").strip()
    if not stripped:
        return None

    if mode == "compose":
        ctx["reengage_message"] = stripped
        _set_ctx(session, ctx)
        if ctx.get("reengage_flow") == "periodic":
            session.state = BotSession.State.ADMIN_REENGAGE_SCHEDULE
            _persist(session, fields=["state", "context"])
            return _reply(
                "Choose schedule for this campaign:",
                buttons=SCHEDULE_BUTTONS,
            )
        session.state = BotSession.State.ADMIN_REENGAGE
        _persist(session, fields=["state", "context"])
        result = send_to_audience(
            session.bot,
            ctx.get("reengage_audience", "global"),
            stripped,
        )
        extra = ""
        if result.get("last_error"):
            extra = f"\nError: {result['last_error']}"
        return _reply(
            f"Sent: {result.get('sent', 0)}\n"
            f"Failed: {result.get('failed', 0)}\n"
            f"Skipped: {result.get('skipped', 0)}{extra}",
            buttons=REENGAGE_MENU_BUTTONS,
        )

    if mode == "offer_title":
        ctx["offer_title"] = stripped
        ctx["reengage_mode"] = "offer_body"
        _set_ctx(session, ctx)
        return _reply("Enter offer body text:", buttons=_btn())

    if mode == "offer_body":
        ctx["offer_body"] = stripped
        ctx.pop("reengage_mode", None)
        _set_ctx(session, ctx)
        session.state = BotSession.State.ADMIN_OFFER_CREATE
        _persist(session, fields=["state", "context"])
        return _reply(
            f"Save offer?\n\nTitle: {ctx.get('offer_title')}\n\n{stripped}",
            buttons=_btn(BTN_ADMIN_OFFER_SAVE),
        )

    return None


def handle_admin_action(session: BotSession, action: str | None) -> dict | None:
    """
    Handle admin panel actions. Returns None if the action is not admin-related
    (caller should continue the customer FSM).
    """
    staff = staff_for_session(session)
    if staff is None:
        return None

    if action in (None, ""):
        if session.state.startswith("ADMIN"):
            return go_admin_menu(session)
        return None

    if action == CB_ADMIN_HOME:
        return go_admin_menu(session)

    if action == CB_ADMIN_PENDING:
        return _show_request_list(session, kind="pending")

    if action == CB_ADMIN_RECENT:
        return _show_request_list(session, kind="recent")

    if action == CB_ADMIN_STATS:
        return _show_stats(session)

    if action == CB_ADMIN_ANALYTICS:
        return _show_analytics(session)

    if action == CB_ADMIN_CUSTOMER_ANALYSIS:
        return _show_customer_analysis(session)

    if action == CB_ADMIN_REENGAGE:
        return _show_reengage_menu(session)

    if action == CB_ADMIN_ANALYTICS_EXCHANGE:
        session.state = BotSession.State.ADMIN_ANALYTICS_EXCHANGE
        _persist(session, fields=["state"])
        return _reply(
            "Exchange Requests\n\nChoose a filter:",
            buttons=EXCHANGE_MENU_BUTTONS,
        )

    if action == CB_ADMIN_ANALYTICS_MEMBERS:
        session.state = BotSession.State.ADMIN_ANALYTICS_MEMBERS
        _persist(session, fields=["state"])
        return _reply(
            "New members\n\nChoose a period:",
            buttons=MEMBERS_MENU_BUTTONS,
        )

    if action == CB_ADMIN_EXCH_SUCCESS:
        text = format_exchange_requests(session.bot, kind="successful")
        return _reply(text, buttons=EXCHANGE_MENU_BUTTONS)

    if action == CB_ADMIN_EXCH_PENDING:
        text = format_exchange_requests(session.bot, kind="pending")
        return _reply(text, buttons=EXCHANGE_MENU_BUTTONS)

    if action in (
        CB_ADMIN_MEMBERS_1,
        CB_ADMIN_MEMBERS_3,
        CB_ADMIN_MEMBERS_9,
        CB_ADMIN_MEMBERS_12,
    ):
        months_map = {
            CB_ADMIN_MEMBERS_1: 1,
            CB_ADMIN_MEMBERS_3: 3,
            CB_ADMIN_MEMBERS_9: 9,
            CB_ADMIN_MEMBERS_12: 12,
        }
        text = format_new_members(session.bot, months_map[action])
        return _reply(text, buttons=MEMBERS_MENU_BUTTONS)

    if action.startswith(CB_ADMIN_AUDIENCE_PREFIX):
        audience = action[len(CB_ADMIN_AUDIENCE_PREFIX) :]
        ctx = _ctx(session)
        ctx["reengage_audience"] = audience
        ctx["reengage_mode"] = "compose"
        is_periodic = ctx.get("reengage_flow") == "periodic"
        is_offer = session.state == BotSession.State.ADMIN_OFFER_CREATE
        if is_offer:
            ctx["reengage_mode"] = "offer_title"
            _set_ctx(session, ctx)
            return _reply(
                f"Audience: {audience}\n\nEnter offer title:",
                buttons=_btn(),
            )
        _set_ctx(session, ctx)
        session.state = BotSession.State.ADMIN_REENGAGE_COMPOSE
        _persist(session, fields=["state", "context"])
        prompt = (
            f"Audience: {audience}\n\nType campaign message:"
            if is_periodic
            else f"Audience: {audience}\n\nType your message to send now:"
        )
        return _reply(prompt, buttons=_btn())

    if action == CB_ADMIN_REENGAGE_PERIODIC:
        ctx = _ctx(session)
        ctx["reengage_flow"] = "periodic"
        ctx["reengage_mode"] = "compose"
        _set_ctx(session, ctx)
        session.state = BotSession.State.ADMIN_REENGAGE_AUDIENCE
        _persist(session, fields=["state", "context"])
        return _reply(
            "Periodic campaign\n\nChoose audience first:",
            buttons=AUDIENCE_BUTTONS,
        )

    if action == CB_ADMIN_REENGAGE_OFFER:
        ctx = _ctx(session)
        ctx["reengage_mode"] = "offer_title"
        ctx["reengage_audience"] = ctx.get("reengage_audience", "global")
        _set_ctx(session, ctx)
        session.state = BotSession.State.ADMIN_OFFER_CREATE
        _persist(session, fields=["state", "context"])
        return _reply(
            "Offer creation\n\nChoose audience (optional, default Global), "
            "then enter title on next message.\n\n"
            "Tap an audience or type offer title:",
            buttons=AUDIENCE_BUTTONS,
        )

    if action.startswith(CB_ADMIN_SCHEDULE_PREFIX):
        schedule = action[len(CB_ADMIN_SCHEDULE_PREFIX) :]
        ctx = _ctx(session)
        message = ctx.get("reengage_message", "").strip()
        audience = ctx.get("reengage_audience", "global")
        if not message:
            return go_admin_menu(session)
        campaign = ReengageCampaign.objects.create(
            bot=session.bot,
            audience=audience,
            message=message,
            schedule=schedule,
            is_active=True,
            next_run_at=timezone.now(),
        )
        schedule_next_run(campaign)
        ctx.pop("reengage_mode", None)
        ctx.pop("reengage_flow", None)
        _set_ctx(session, ctx)
        return _reply(
            f"Campaign saved.\nAudience: {audience}\nSchedule: {schedule}\n"
            f"Next run: {campaign.next_run_at}",
            buttons=REENGAGE_MENU_BUTTONS,
        )

    if action == CB_ADMIN_OFFER_SAVE:
        ctx = _ctx(session)
        title = (ctx.get("offer_title") or "").strip()
        body = (ctx.get("offer_body") or "").strip()
        audience = ctx.get("reengage_audience", "global")
        if not title or not body:
            return _reply("Offer title and body required.", buttons=_btn())
        offer = ReengageOffer.objects.create(
            bot=session.bot,
            title=title,
            body=body,
            audience=audience,
            is_active=True,
        )
        ctx.pop("offer_title", None)
        ctx.pop("offer_body", None)
        _set_ctx(session, ctx)
        return _reply(
            f"Offer saved: {offer.title}\nAudience: {audience}",
            buttons=REENGAGE_MENU_BUTTONS,
        )

    if action == CB_ADMIN_BACK_LIST:
        kind = _ctx(session).get("admin_list_kind") or "pending"
        return _show_request_list(session, kind=kind)

    if action == CB_ADMIN_BACK_DETAIL:
        req = _load_admin_request(session)
        if req is None:
            return go_admin_menu(session)
        return _show_request_detail(session, req)

    if action.startswith(CB_ADMIN_OPEN_PREFIX):
        try:
            req_id = int(action[len(CB_ADMIN_OPEN_PREFIX) :])
        except ValueError:
            return go_admin_menu(session)
        req = (
            ExchangeRequest.objects.select_related("customer")
            .filter(pk=req_id, bot=session.bot)
            .first()
        )
        if req is None:
            return _reply("Request not found.", buttons=_btn())
        return _show_request_detail(session, req)

    if action == CB_ADMIN_CHANGE_STATE:
        return _show_change_state(session)

    if action == CB_ADMIN_HOLD:
        req = _load_admin_request(session)
        if req is None:
            return go_admin_menu(session)
        ttl = hold_request(req)
        req.refresh_from_db()
        out = _show_request_detail(session, req)
        out["text"] = f"TTL increase : {ttl}\n\n" + (out.get("text") or "")
        return out

    if action.startswith(CB_ADMIN_STATE_PREFIX):
        status = action[len(CB_ADMIN_STATE_PREFIX) :]
        req = _load_admin_request(session)
        if req is None:
            return go_admin_menu(session)
        try:
            set_request_status(req, status)
        except ValueError:
            return _show_change_state(session)
        req.refresh_from_db()
        out = _show_request_detail(session, req)
        out["text"] = (
            f"Request #{req.pk} is now {req.get_status_display()}.\n\n"
            + (out.get("text") or "")
        )
        return out

    if action == CB_ADMIN_TAG:
        return _show_tag_user_list(session)

    if action.startswith(CB_ADMIN_TAG_USER_PREFIX):
        try:
            tid = int(action[len(CB_ADMIN_TAG_USER_PREFIX) :])
        except ValueError:
            return _show_tag_user_list(session)
        profile = CustomerProfile.objects.filter(telegram_user_id=tid).first()
        if profile is None:
            return _reply("User not found.", buttons=_btn(BTN_ADMIN_TAG))
        return _show_tag_choices(session, profile)

    if action.startswith(CB_ADMIN_TAG_PREFIX):
        tag = action[len(CB_ADMIN_TAG_PREFIX) :]
        ctx = _ctx(session)
        tid = ctx.get("admin_tag_telegram_id")
        if not tid:
            return _show_tag_user_list(session)
        profile = CustomerProfile.objects.filter(telegram_user_id=tid).first()
        if profile is None:
            return _reply("User not found.", buttons=_btn(BTN_ADMIN_TAG))
        try:
            set_customer_tag(profile, tag)
        except AdminTagImmutable:
            return _reply(
                "Admin tag cannot be changed.",
                buttons=_btn(BTN_ADMIN_TAG),
            )
        except ValueError:
            return _show_tag_choices(session, profile)
        ctx.pop("admin_tag_telegram_id", None)
        _set_ctx(session, ctx)
        _persist(session, fields=["context"])
        return _reply(
            f"Tag updated.\nUser {profile.telegram_user_id} is now {tag}.",
            buttons=_btn(BTN_ADMIN_TAG),
        )

    if action == CB_ADMIN_CLOSE:
        return go_admin_menu(session)

    if session.state.startswith("ADMIN"):
        return go_admin_menu(session)

    return None


def handle_admin_text(session: BotSession, text: str) -> dict | None:
    """Handle free-text input during admin compose flows."""
    if not session.state.startswith("ADMIN"):
        return None
    stripped = (text or "").strip()
    if session.state == BotSession.State.ADMIN_SET_TAG:
        if stripped in ("◀ Prev", "Next ▶"):
            ctx = _ctx(session)
            page = int(ctx.get("tag_page") or 0)
            ctx["tag_page"] = max(0, page - 1) if stripped == "◀ Prev" else page + 1
            _set_ctx(session, ctx)
            return _show_tag_user_list(session)
        if stripped.isdigit():
            profile = CustomerProfile.objects.filter(
                telegram_user_id=int(stripped)
            ).first()
            if profile is None:
                return _reply(
                    f"User {stripped} not found.\n\n{TAG_PROMPT}",
                    buttons=_btn(BTN_ADMIN_TAG),
                )
            return _show_tag_choices(session, profile)
        return _show_tag_user_list(session)
    if session.state in (
        BotSession.State.ADMIN_REENGAGE_COMPOSE,
        BotSession.State.ADMIN_OFFER_CREATE,
    ):
        return _handle_reengage_text(session, text)
    if session.state == BotSession.State.ADMIN_REENGAGE_AUDIENCE:
        ctx = _ctx(session)
        if ctx.get("reengage_flow") == "periodic":
            return _handle_reengage_text(session, text)
    return None
