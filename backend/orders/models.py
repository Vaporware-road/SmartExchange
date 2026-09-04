import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from bot_gateway.models import BotCustomer, Platform
from category.models import Category, PriceType


class OrderIntake(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    class TradeType(models.TextChoices):
        BUY = "buy", "Buy"
        SELL = "sell", "Sell"

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    customer = models.ForeignKey(
        BotCustomer, on_delete=models.CASCADE, related_name="orders"
    )
    platform = models.CharField(max_length=16, choices=Platform.choices)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.PENDING, db_index=True
    )
    trade_type = models.CharField(max_length=8, choices=TradeType.choices)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="order_intakes"
    )
    price_type = models.ForeignKey(
        PriceType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_intakes",
    )
    amount = models.DecimalField(max_digits=18, decimal_places=4)
    currency_code = models.CharField(max_length=16, blank=True)
    customer_note = models.TextField(blank=True)
    admin_note = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_orders",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    source_metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = "Order Intake"
        verbose_name_plural = "Order Intakes"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.uuid} ({self.status})"
