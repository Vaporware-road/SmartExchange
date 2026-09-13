from django.contrib import admin

from .models import WebsiteAsset, WebsitePublication, WebsiteSection, WebsiteSite


class WebsiteSectionInline(admin.TabularInline):
    model = WebsiteSection
    extra = 0
    fields = ("section_type", "key", "order", "is_enabled", "variant")


@admin.register(WebsiteSite)
class WebsiteSiteAdmin(admin.ModelAdmin):
    list_display = ("slug", "status", "layout_slug", "theme_slug", "published_version", "published_at")
    list_filter = ("status", "layout_slug", "theme_slug")
    search_fields = ("slug",)
    inlines = [WebsiteSectionInline]


@admin.register(WebsitePublication)
class WebsitePublicationAdmin(admin.ModelAdmin):
    list_display = ("site", "version", "published_at", "published_by", "note")
    list_filter = ("published_at",)


@admin.register(WebsiteAsset)
class WebsiteAssetAdmin(admin.ModelAdmin):
    list_display = ("image", "site", "role", "width", "height", "created_at")
    list_filter = ("role",)
