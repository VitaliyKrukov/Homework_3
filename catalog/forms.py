from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_purchase_price(self):

        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price is None:
            raise ValidationError('Поле "Цена покупки" обязательно для заполнения.')
        if purchase_price < 0:
            raise ValidationError("Цена должна быть положительным числом.")
        return purchase_price

    def clean(self):
        FORBIDDEN_WORDS = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        if name:
            found_forbidden_words = [
                word for word in FORBIDDEN_WORDS if word in name.lower()
            ]
            if found_forbidden_words:
                self.add_error(
                    "name",
                    f'Название содержит запрещенные слова: {", ".join(found_forbidden_words)}',
                )
        if description:
            found_forbidden_words = [
                word for word in FORBIDDEN_WORDS if word in description.lower()
            ]
            if found_forbidden_words:
                self.add_error(
                    "description",
                    f'Описание содержит запрещенные слова: {", ".join(found_forbidden_words)}',
                )
        return cleaned_data
