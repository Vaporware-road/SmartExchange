from django.test import TestCase
from rest_framework.exceptions import ValidationError as DRFValidationError

from category.models import Category, Currency, PriceType
from template_editor.api_views import _validate_template_price_bindings
from template_editor.models import Template


class TemplateBindingValidationTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="EUR")
        self.other_category = Category.objects.create(name="USDT")
        self.eur, _ = Currency.objects.get_or_create(code="EUR", defaults={"name": "Euro"})
        self.irr, _ = Currency.objects.get_or_create(code="IRR", defaults={"name": "Rial"})
        self.gbp, _ = Currency.objects.get_or_create(code="GBP", defaults={"name": "Pound"})
        self.valid_pt = PriceType.objects.create(
            category=self.category,
            name="Buy EUR",
            source_currency=self.eur,
            target_currency=self.irr,
            trade_type="buy",
        )
        self.invalid_pt = PriceType.objects.create(
            category=self.other_category,
            name="Sell GBP",
            source_currency=self.gbp,
            target_currency=self.irr,
            trade_type="sell",
        )
        self.template = Template.objects.create(name="eur-template", category=self.category)

    def test_accepts_config_without_price_binding_draft(self):
        _validate_template_price_bindings(
            self.template,
            {
                "widgets": [
                    {
                        "id": "a1",
                        "type": "text",
                        "x": "10%",
                        "y": "10%",
                        "width": "20%",
                        "height": "10%",
                        "style": {},
                    }
                ]
            },
        )

    def test_rejects_price_binding_from_another_category(self):
        with self.assertRaises(DRFValidationError):
            _validate_template_price_bindings(
                self.template,
                {
                    "widgets": [
                        {
                            "id": "a1",
                            "type": "text",
                            "x": "10%",
                            "y": "10%",
                            "width": "20%",
                            "height": "10%",
                            "style": {"priceTypeId": self.invalid_pt.id},
                        }
                    ]
                },
            )

    def test_accepts_valid_category_price_binding(self):
        _validate_template_price_bindings(
            self.template,
            {
                "widgets": [
                    {
                        "id": "a1",
                        "type": "text",
                        "x": "10%",
                        "y": "10%",
                        "width": "20%",
                        "height": "10%",
                        "style": {"priceTypeId": self.valid_pt.id},
                    }
                ]
            },
        )
