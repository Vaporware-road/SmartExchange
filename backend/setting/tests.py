from django.test import TestCase

from setting.models import SiteSettings
from setting.serializers import SiteSettingsSerializer


class SiteSettingsUiFontValidationTest(TestCase):
    def test_empty_ui_fonts_allowed(self):
        s = SiteSettingsSerializer(
            instance=SiteSettings.load(),
            data={
                "ui_font_filename_rtl": "",
                "ui_font_filename_ltr": "",
            },
            partial=True,
        )
        self.assertTrue(s.is_valid(), s.errors)

    def test_unknown_font_rejected(self):
        s = SiteSettingsSerializer(
            instance=SiteSettings.load(),
            data={"ui_font_filename_rtl": "definitely-missing-file-xyz.ttf"},
            partial=True,
        )
        self.assertFalse(s.is_valid())
        self.assertIn("ui_font_filename_rtl", s.errors)
