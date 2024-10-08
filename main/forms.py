from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]

    def clean_product_name(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_product_description(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)
