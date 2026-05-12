"""Tests for Instagram Hub caption extras and publication logging helpers."""

from django.test import TestCase

from instagram_hub.models import InstagramConfig
from instagram_hub.tasks import _feed_caption_with_config_extras


class InstagramCaptionExtrasTest(TestCase):
    def test_suffix_and_hashtags_appended_under_cap(self):
        cfg = InstagramConfig.objects.create(
            name="cfg1",
            is_active=True,
            ig_user_id="123456789",
            feed_caption_suffix="Second line",
            feed_hashtags="#fx #rates",
        )
        cfg.set_access_token("dummy-token")
        cfg.save()

        out = _feed_caption_with_config_extras("عنوان")
        self.assertIn("عنوان", out)
        self.assertIn("Second line", out)
        self.assertIn("#fx", out)
        self.assertLessEqual(len(out), 2200)

    def test_long_hashtags_truncated_to_caption_max(self):
        cfg = InstagramConfig.objects.create(
            name="cfg2",
            is_active=True,
            ig_user_id="987654321",
            feed_caption_suffix="",
            feed_hashtags="x" * 5000,
        )
        cfg.set_access_token("dummy-token")
        cfg.save()

        out = _feed_caption_with_config_extras("Hi")
        self.assertEqual(len(out), 2200)
