# Cache signals removed - no caching is used in this application
# If you need to add signals for other purposes, you can add them here

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Currency


@receiver(post_migrate)
def create_default_currencies_on_startup(sender, **kwargs):
    """
    Ensure default currencies are created when the app starts.
    This runs after migrations to guarantee currencies exist.
    """
    # Only run for the category app
    if sender.name != 'category':
        return
    
    # List of commonly used currencies in the website
    default_currencies = [
        {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
        {'code': 'EUR', 'name': 'Euro', 'symbol': '€'},
        {'code': 'GBP', 'name': 'British Pound', 'symbol': '£'},
        {'code': 'IRR', 'name': 'Iranian Rial', 'symbol': '﷼'},
        {'code': 'IRT', 'name': 'Iranian Toman', 'symbol': 'تومان'},
        {'code': 'USDT', 'name': 'Tether', 'symbol': 'USDT'},
        {'code': 'AED', 'name': 'UAE Dirham', 'symbol': 'د.إ'},
        {'code': 'TRY', 'name': 'Turkish Lira', 'symbol': '₺'},
        {'code': 'CAD', 'name': 'Canadian Dollar', 'symbol': 'C$'},
        {'code': 'AUD', 'name': 'Australian Dollar', 'symbol': 'A$'},
        {'code': 'JPY', 'name': 'Japanese Yen', 'symbol': '¥'},
        {'code': 'CHF', 'name': 'Swiss Franc', 'symbol': 'CHF'},
    ]
    
    # Create currencies if they don't exist
    for currency_data in default_currencies:
        Currency.objects.get_or_create(
            code=currency_data['code'],
            defaults={
                'name': currency_data['name'],
                'symbol': currency_data['symbol']
            }
        )

