from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f"{self.code} ({self.symbol})" if self.symbol else self.code


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    # Telegram message content for this category
    telegram_message_description = models.TextField(blank=True, null=True)
    telegram_media_url = models.URLField(max_length=500, blank=True)
    inline_buttons = models.JSONField(default=list, blank=True)  # [{"label": "...", "url": "..."}]
    last_used_template = models.ForeignKey(
        "template_editor.Template",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        help_text="Last template_editor.Template used for round-robin price image publishing.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True) or "category"
            slug = base_slug
            counter = 1

            # Loop until we find a unique slug
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def clean(self):
        validate_category_buy_sell_spread(self)

    def __str__(self):
        return self.name



class PriceType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='price_types')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, blank=True)
    # Currency pair and trade direction
    source_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, related_name='+')
    target_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, related_name='+')
    TRADE_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )
    trade_type = models.CharField(max_length=10, choices=TRADE_CHOICES)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PriceType"
        verbose_name_plural = "PriceTypes"
        ordering = ['order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['category', 'name'], name='unique_category_pricetype_name'),
        ]

    def save(self, *args, **kwargs):
        # Ensure slug is unique within the same category
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=True) or 'pricetype'
            slug = base_slug
            counter = 1
            while PriceType.objects.filter(category=self.category, slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


def validate_category_buy_sell_spread(category, prices_map=None):
    """
    For the given category, ensure that for each (source_currency, target_currency) pair
    that has both buy and sell price types, the sell price is >= buy price.
    prices_map: optional dict mapping price_type_id (int or str) -> Decimal price.
    If None, latest prices from DB are used.
    """
    from decimal import Decimal
    price_types = PriceType.objects.filter(category=category).select_related(
        "source_currency", "target_currency"
    ).prefetch_related("price_histories")
    pair_to_types = {}
    for pt in price_types:
        key = (pt.source_currency_id, pt.target_currency_id)
        if key not in pair_to_types:
            pair_to_types[key] = {"buy": [], "sell": []}
        if prices_map is not None:
            price = prices_map.get(pt.id) or prices_map.get(str(pt.id))
            if price is not None:
                pair_to_types[key][pt.trade_type].append((pt, Decimal(str(price))))
            else:
                latest = pt.price_histories.first()
                pair_to_types[key][pt.trade_type].append((pt, latest.price if latest else None))
        else:
            latest = pt.price_histories.first()
            pair_to_types[key][pt.trade_type].append((pt, latest.price if latest else None))
    for key, by_trade in pair_to_types.items():
        buy_data = by_trade.get("buy") or []
        sell_data = by_trade.get("sell") or []
        if not buy_data or not sell_data:
            continue
        buy_prices = [price for _, price in buy_data if price is not None]
        sell_prices = [price for _, price in sell_data if price is not None]
        if not buy_prices or not sell_prices:
            continue
        highest_buy = max(buy_prices)
        lowest_sell = min(sell_prices)
        if lowest_sell < highest_buy:
            raise ValidationError(
                "Sell price (%s) cannot be lower than buy price (%s) for the same currency pair in category \"%s\"."
                % (lowest_sell, highest_buy, category.name)
            )
