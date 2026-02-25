# SmartExchange Panel – Master Plan

## Phase 1: Rebranding & Cleanup ✅ COMPLETED

### 1.1 Global Rebrand
- **README**: Pardis Panel → SmartExchange Panel
- **Project structure docs**: PardisPanel → SmartExchangePanel
- **Links**: Removed hardcoded sarafipardis.co.uk URLs; replaced with "configure in deployment"
- **base.html**: Page title uses `{{ site_settings.site_name }} Panel`
- **SiteSettings default**: `site_name = "SmartExchange"`
- **Note**: Django project folder `SarafiPardis/` left unchanged to avoid breaking imports and deployments

### 1.2 UI Cleanup – Hardcoded Contact Data Removed
- **price_publisher/services/publisher.py**: All contact info now comes from `SiteSettings`
  - `_build_contact_section()` → uses `support_phone`
  - `_build_common_description()` → uses `address`, `office_map_url`, `business_hours`
  - `_build_tether_caption()` → uses `support_phone`, `support_phone_2`, `support_phone_3`, `address`, `office_map_url`, `business_hours`, `site_name`
  - `_build_gbp_category_caption()` → same fields
  - `_build_legacy_final_message()` → dynamic from SiteSettings
  - `_build_legacy_final_buttons()` → dynamic from SiteSettings
- **price_publisher/services/telegram_templates.py**: Replaced hardcoded PARDIS_* constants with `get_legacy_caption_from_settings()` and `get_legacy_buttons_from_settings()`
- **Footer** (templates/partials/footer.html): Already used `site_settings` for all contact info – no changes needed

### 1.3 Dynamic Branding
- **SiteSettings model** (`setting/models.py`):
  - Existing: `logo`, `favicon`, `support_phone`, `support_email`, `address`, social links
  - New: `office_map_url`, `business_hours`, `support_phone_2`, `support_phone_3`
- **Migration**: `setting/migrations/0004_add_office_and_contact_fields.py`
- **base.html**: Favicon uses `site_settings.favicon.url` when set, else static fallback
- **navbar.html**: Logo uses `site_settings.logo.url` when set, else icon + site name
- **Django Admin**: `SiteSettingsAdmin` updated with fieldsets (Branding, Contact, Office & Business, Social Links)
- **API/Serializers**: New fields exposed in `SiteSettingsSerializer`
- **Vue store**: `siteSettings.js` state extended with new fields

### Where to Configure
- **Django Admin** (`/admin/setting/sitesettings/`): Upload logo, favicon, set support phone(s), office address, map URL, business hours
- **API** (`PUT /api/settings/site/`): Update from Vue frontend when branding UI is added

---

## Phase 2: Backend API Conversion (NEXT)

1. Audit current Django views (`/dashboard/`, `/category/`, `/prices/`, `/finalize/`, `/settings/`)
2. Convert HTML-rendering views to DRF API ViewSets/Endpoints
3. Ensure Session or JWT auth for Vue frontend
4. Fix any flow logic bugs (Telegram publishing, External API sync)

---

## Phase 3: Vue.js Frontend Development

1. Initialize Vue 3 project (already present in `/frontend/`)
2. Rebuild UI with responsive design (Tailwind CSS)
3. Connect Vue app to DRF endpoints
4. Replace old templates

---

## Phase 4: Deprecation & Final Testing

1. Remove old Django templates
2. End-to-end tests: Update → Finalize → Render Image → Publish to Telegram

---

## Run Migration

```bash
python manage.py migrate setting
```
