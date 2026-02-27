from django.db import models
from django.core.cache import cache
from django.utils import timezone


class PriceThemeState(models.Model):
    """
    Tracks the last price theme index used when rendering channel images.

    A single row with key ``price_theme`` is created automatically and updated
    each time a new image is rendered so that themes cycle through sequentially.
    """

    key = models.CharField(max_length=50, unique=True)
    last_index = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Price Theme State"
        verbose_name_plural = "Price Theme States"

    @classmethod
    def get_or_create_theme_state(cls):
        return cls.objects.get_or_create(key="price_theme", defaults={"last_index": 0})


class Log(models.Model):
    """
    Stores application logs from various sources (Telegram, Finalize, etc.)
    """
    
    LEVEL_CHOICES = [
        ('DEBUG', 'Debug'),
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
        ('CRITICAL', 'Critical'),
    ]
    
    SOURCE_CHOICES = [
        ('telegram', 'Telegram'),
        ('finalize', 'Finalize'),
        ('price_publisher', 'Price Publisher'),
        ('template_editor', 'Template Editor'),
        ('external_api', 'External API'),
        ('system', 'System'),
        ('other', 'Other'),
    ]
    
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='INFO')
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default='system')
    message = models.TextField(verbose_name="Message")
    details = models.TextField(blank=True, null=True, verbose_name="Additional Details")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logs',
        verbose_name="User"
    )
    
    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['level', '-created_at']),
            models.Index(fields=['source', '-created_at']),
        ]
    
    def __str__(self):
        return f"[{self.level}] {self.source} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class SiteSettings(models.Model):
    """
    Singleton model for dynamic branding and contact information.
    Only one row should exist; use ``SiteSettings.load()`` to retrieve it.
    """

    site_name = models.CharField(max_length=100, default="SmartExchange")
    tagline = models.CharField(max_length=200, default="Premium Exchange Panel")
    logo = models.ImageField(upload_to="branding/", null=True, blank=True)
    favicon = models.ImageField(upload_to="branding/", null=True, blank=True)
    support_phone = models.CharField(max_length=30, blank=True)
    support_email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    office_map_url = models.URLField(
        blank=True,
        help_text="Google Maps or similar URL for office location (used in Telegram captions)",
    )
    business_hours = models.TextField(
        blank=True,
        default="دوشنبه تا شنبه: 9:30 صبح تا ۱۷\nیکشنبه ها: تعطیل",
        help_text="Business hours text (Persian/English) for Telegram captions",
    )
    support_phone_2 = models.CharField(max_length=30, blank=True)
    support_phone_3 = models.CharField(max_length=30, blank=True)
    telegram_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    auto_post_on_update = models.BooleanField(
        default=False,
        help_text=(
            "If enabled, finalized prices can be auto-posted when updates occur. "
            "A scheduler must read this flag and trigger publishing."
        ),
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        cache.delete("site_settings")

    @classmethod
    def load(cls):
        cached = cache.get("site_settings")
        if cached:
            return cached
        obj, _ = cls.objects.get_or_create(pk=1)
        cache.set("site_settings", obj, timeout=300)
        return obj

