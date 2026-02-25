from datetime import timedelta

from django.db.models import Prefetch
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category, PriceType
from change_price.models import PriceHistory
from special_price.models import SpecialPriceType, SpecialPriceHistory
from telegram_app.models import TelegramBot, TelegramChannel


class DashboardSummaryAPIView(APIView):

    def get(self, request):
        now = timezone.now()
        twenty_four_hours_ago = now - timedelta(hours=24)

        highest_price_obj = (
            PriceHistory.objects.select_related("price_type")
            .order_by("-price")
            .first()
        )
        highest_price = float(highest_price_obj.price) if highest_price_obj else 0
        highest_price_label = (
            highest_price_obj.price_type.name if highest_price_obj else "N/A"
        )

        price_changes = []
        price_types = PriceType.objects.prefetch_related("price_histories").all()
        for pt in price_types:
            latest = pt.price_histories.first()
            if not latest:
                continue
            old = (
                pt.price_histories.filter(created_at__lte=twenty_four_hours_ago)
                .order_by("-created_at")
                .first()
            )
            if old and latest.created_at > twenty_four_hours_ago:
                current_price = float(latest.price)
                old_price = float(old.price)
                if old_price > 0:
                    change_pct = ((current_price - old_price) / old_price) * 100
                    price_changes.append({
                        "name": pt.name,
                        "current": current_price,
                        "old": old_price,
                        "change_percent": round(change_pct, 2),
                        "change_amount": round(current_price - old_price, 2),
                    })

        avg_24h_change = 0
        biggest_change = None
        if price_changes:
            avg_24h_change = round(
                sum(p["change_percent"] for p in price_changes) / len(price_changes), 2
            )
            biggest_change = max(price_changes, key=lambda x: abs(x["change_percent"]))

        total_bots = TelegramBot.objects.count()
        active_bots = TelegramBot.objects.filter(is_active=True).count()
        total_channels = TelegramChannel.objects.count()
        active_channels = TelegramChannel.objects.filter(is_active=True).count()
        total_price_types = PriceType.objects.count()
        total_price_updates = PriceHistory.objects.count()

        latest_update = PriceHistory.objects.order_by("-created_at").first()
        latest_update_time = latest_update.created_at.isoformat() if latest_update else None

        recent_updates = PriceHistory.objects.filter(
            created_at__gte=twenty_four_hours_ago
        ).count()

        return Response({
            "highest_price": highest_price,
            "highest_price_label": highest_price_label,
            "avg_24h_change": avg_24h_change,
            "biggest_change": biggest_change,
            "price_changes": price_changes,
            "total_bots": total_bots,
            "active_bots": active_bots,
            "total_channels": total_channels,
            "active_channels": active_channels,
            "total_price_types": total_price_types,
            "total_price_updates": total_price_updates,
            "latest_update_time": latest_update_time,
            "recent_updates_24h": recent_updates,
        })
