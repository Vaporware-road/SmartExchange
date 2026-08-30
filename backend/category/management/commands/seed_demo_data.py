"""
Seed professional demo data for Categories, PriceTypes, SpecialPriceTypes, and Pending Finalize state.

- Categories: Tether (USDT), British Pound (GBP), Euro (EUR) with pairs USDT/IRT, GBP/IRT, EUR/IRT.
- Each category has at least 2 price types (Buy/Sell) for Dual-Column Bulk Update layout.
- Special Prices: "Cash VIP Buy" (Gold Star icon), "Corporate Sell" (Shield icon).
- Realistic market rates (USDT ~65,000 range).
- Creates 2–3 pending updates (old price finalized, new price not) for FinalizeView testing.

- Telegram: one demo bot and channel, so the finalize wizard can be walked end to end.

Usage:
  python manage.py seed_demo_data
  python manage.py seed_demo_data --clear      # Remove demo categories/special types created by this command first
  python manage.py seed_demo_data --if-empty   # No-op when the panel already has categories (safe on every boot)
"""
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from category.models import Category, Currency, PriceType
from change_price.models import PriceHistory
from finalize.models import Finalization, FinalizedPriceHistory
from special_price.models import SpecialPriceHistory, SpecialPricePair, SpecialPriceType
from telegram_app.models import TelegramBot, TelegramChannel


# Slug used to mark categories created by this command (for --clear)
DEMO_CATEGORY_SLUG_PREFIX = "demo-"
# Exact names for special prices (cleared with --clear)
DEMO_SPECIAL_NAMES = ("Cash VIP Buy", "Corporate Sell")
# Demo Telegram bot/channel. The token is deliberately not a real one: the demo
# must show the publish step without ever reaching a customer's channel.
DEMO_BOT_NAME = "Demo Bot"
DEMO_BOT_TOKEN = "000000000:DEMO-BOT-TOKEN-NOT-A-REAL-CREDENTIAL"
DEMO_CHANNEL_NAME = "Demo Rates Channel"
DEMO_CHANNEL_CHAT_ID = "@mrexchange_demo"


def create_telegram_demo_channel():
    """A bot and channel so Finalize offers a publish target instead of an empty state."""
    bot, _ = TelegramBot.objects.get_or_create(
        name=DEMO_BOT_NAME,
        defaults={
            "token": DEMO_BOT_TOKEN,
            "display_name": "MrExchange Demo",
            "is_active": True,
            "notes": "Seeded demo bot — not connected to Telegram.",
        },
    )
    TelegramChannel.objects.get_or_create(
        bot=bot,
        chat_id=DEMO_CHANNEL_CHAT_ID,
        defaults={"name": DEMO_CHANNEL_NAME, "is_active": True},
    )


def get_currency(code: str) -> Currency:
    return Currency.objects.get(code=code)


def ensure_currencies():
    """Ensure USDT, GBP, EUR, IRT exist (created by category signals)."""
    for code in ("USDT", "GBP", "EUR", "IRT"):
        Currency.objects.get_or_create(
            code=code,
            defaults={
                "name": {
                    "USDT": "Tether",
                    "GBP": "British Pound",
                    "EUR": "Euro",
                    "IRT": "Iranian Toman",
                }.get(code, code),
                "symbol": code,
            },
        )


def clear_demo_data():
    """Remove categories and special price types created by this command."""
    Category.objects.filter(slug__startswith=DEMO_CATEGORY_SLUG_PREFIX).delete()
    SpecialPriceType.objects.filter(name__in=DEMO_SPECIAL_NAMES).delete()
    TelegramBot.objects.filter(name=DEMO_BOT_NAME).delete()


def create_categories_and_prices(currencies):
    """Create Tether, British Pound, Euro categories with pairs and price types.

    Only the XXX/IRT direction is seeded: PriceHistory.price is a 2-decimal
    field, so an inverse rate such as 0.0000121 would store — and the demo would
    display — 0.00.
    """
    USDT = currencies["USDT"]
    GBP = currencies["GBP"]
    EUR = currencies["EUR"]
    IRT = currencies["IRT"]

    categories_config = [
        {
            "name": "Tether (USDT)",
            "slug": f"{DEMO_CATEGORY_SLUG_PREFIX}tether-usdt",
            "description": "Tether USDT pairs with Iranian Toman.",
            "pairs": [
                {"name": "USDT/IRT Buy", "source": USDT, "target": IRT, "trade_type": "buy", "order": 0},
                {"name": "USDT/IRT Sell", "source": USDT, "target": IRT, "trade_type": "sell", "order": 1},
            ],
            "prices": {
                "USDT/IRT Buy": Decimal("64800.00"),
                "USDT/IRT Sell": Decimal("65200.00"),
            },
        },
        {
            "name": "British Pound (GBP)",
            "slug": f"{DEMO_CATEGORY_SLUG_PREFIX}gbp",
            "description": "British Pound pairs with Iranian Toman.",
            "pairs": [
                {"name": "GBP/IRT Buy", "source": GBP, "target": IRT, "trade_type": "buy", "order": 0},
                {"name": "GBP/IRT Sell", "source": GBP, "target": IRT, "trade_type": "sell", "order": 1},
            ],
            "prices": {
                "GBP/IRT Buy": Decimal("82500.00"),
                "GBP/IRT Sell": Decimal("83200.00"),
            },
        },
        {
            "name": "Euro (EUR)",
            "slug": f"{DEMO_CATEGORY_SLUG_PREFIX}euro",
            "description": "Euro pair with Iranian Toman.",
            "pairs": [
                {"name": "EUR/IRT Buy", "source": EUR, "target": IRT, "trade_type": "buy", "order": 0},
                {"name": "EUR/IRT Sell", "source": EUR, "target": IRT, "trade_type": "sell", "order": 1},
            ],
            "prices": {
                "EUR/IRT Buy": Decimal("69800.00"),
                "EUR/IRT Sell": Decimal("70400.00"),
            },
        },
    ]

    created_categories = []
    for cfg in categories_config:
        category, _ = Category.objects.get_or_create(
            slug=cfg["slug"],
            defaults={
                "name": cfg["name"],
                "description": cfg.get("description", ""),
            },
        )
        created_categories.append((category, cfg))

    price_types_with_old_history = []
    for category, cfg in created_categories:
        for pair in cfg["pairs"]:
            price_type, _ = PriceType.objects.get_or_create(
                category=category,
                name=pair["name"],
                defaults={
                    "source_currency": pair["source"],
                    "target_currency": pair["target"],
                    "trade_type": pair["trade_type"],
                    "order": pair["order"],
                    "is_active": True,
                },
            )
            price = cfg["prices"].get(pair["name"])
            if price is not None:
                # Create initial (old) price history only if none exists (idempotent)
                if not price_type.price_histories.exists():
                    old_ph = PriceHistory.objects.create(
                        price_type=price_type,
                        price=price,
                        notes="Seed demo initial price",
                    )
                    price_types_with_old_history.append((price_type, old_ph, price))

    return created_categories, price_types_with_old_history


def create_pending_finalize_state(created_categories, price_types_with_old_history):
    """
    For the first category (Tether), create a finalization with the old prices,
    then add new price history for 2–3 price types so they appear as Pending (Old vs New) in FinalizeView.
    Skips if category already has a finalization (idempotent).
    """
    if not created_categories:
        return
    category, cfg = created_categories[0]
    if Finalization.objects.filter(category=category).exists():
        return
    # Select 2–3 price types from this category to have pending updates
    tether_entries = [(pt, old_ph, old_price) for pt, old_ph, old_price in price_types_with_old_history if pt.category_id == category.id][:3]
    if not tether_entries:
        return

    finalization = Finalization.objects.create(
        category=category,
        channel=None,
        finalized_by=None,
        message_sent=False,
        notes="Demo: previous snapshot for pending comparison",
    )
    for price_type, old_ph, _ in tether_entries:
        FinalizedPriceHistory.objects.get_or_create(
            finalization=finalization,
            price_history=old_ph,
        )

    # New prices slightly different to show Old vs New in FinalizeView
    new_prices = {
        "USDT/IRT Buy": Decimal("64950.00"),
        "USDT/IRT Sell": Decimal("65350.00"),
    }
    for price_type, _old_ph, _ in tether_entries:
        new_price = new_prices.get(price_type.name)
        if new_price is not None:
            PriceHistory.objects.create(
                price_type=price_type,
                price=new_price,
                notes="Demo: pending update for FinalizeView",
            )


def create_special_prices(currencies):
    """Create 'Cash VIP Buy' (Gold Star) and 'Corporate Sell' (Shield) special price types."""
    USDT = currencies["USDT"]
    IRT = currencies["IRT"]

    special_config = [
        {
            "name": "Cash VIP Buy",
            "source": USDT,
            "target": IRT,
            "trade_type": "buy",
            "icon": "fas fa-star",
            "price": Decimal("64600.00"),
        },
        {
            "name": "Corporate Sell",
            "source": USDT,
            "target": IRT,
            "trade_type": "sell",
            "icon": "fas fa-shield-alt",
            "price": Decimal("65400.00"),
        },
    ]

    for cfg in special_config:
        spt, created = SpecialPriceType.objects.get_or_create(
            name=cfg["name"],
            defaults={
                "source_currency": cfg["source"],
                "target_currency": cfg["target"],
                "trade_type": cfg["trade_type"],
                "icon": cfg.get("icon", ""),
                "description": "Demo special price for UI testing.",
            },
        )
        if created or not spt.special_price_histories.exists():
            pair, _ = SpecialPricePair.objects.get_or_create(
                special_price_type=spt,
                source_currency=cfg["source"],
                target_currency=cfg["target"],
            )
            SpecialPriceHistory.objects.create(
                special_price_type=spt,
                pair=pair,
                price=cfg["price"],
                notes="Seed demo special price",
            )


class Command(BaseCommand):
    help = "Seed demo data: Categories (USDT, GBP, EUR), Special Prices (Cash VIP Buy, Corporate Sell), and 2–3 Pending finalize updates."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Remove demo categories and special price types created by this command before seeding.",
        )
        parser.add_argument(
            "--if-empty",
            action="store_true",
            help="Seed only when no categories exist yet, so container start-up can run this every boot.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options.get("if_empty") and Category.objects.exists():
            self.stdout.write(
                self.style.NOTICE("Panel already has categories; --if-empty made this a no-op.")
            )
            return

        if options.get("clear"):
            clear_demo_data()
            self.stdout.write(self.style.WARNING("Cleared existing demo data."))

        ensure_currencies()
        currencies = {c.code: c for c in Currency.objects.filter(code__in=["USDT", "GBP", "EUR", "IRT"])}
        if len(currencies) != 4:
            self.stdout.write(self.style.ERROR("Missing one of USDT, GBP, EUR, IRT. Run migrations and ensure category signals run."))
            return

        created_categories, price_types_with_old_history = create_categories_and_prices(currencies)
        create_pending_finalize_state(created_categories, price_types_with_old_history)
        create_special_prices(currencies)
        create_telegram_demo_channel()

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
        self.stdout.write("  - Categories: Tether (USDT), British Pound (GBP), Euro (EUR) with pairs and Buy/Sell price types.")
        self.stdout.write("  - Special Prices: Cash VIP Buy (Gold Star), Corporate Sell (Shield).")
        self.stdout.write("  - 2–3 Pending updates on Tether category for FinalizeView (Old vs New price).")
        self.stdout.write(f"  - Telegram: bot \"{DEMO_BOT_NAME}\" and channel {DEMO_CHANNEL_CHAT_ID} (not connected to Telegram).")
