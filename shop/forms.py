from django import forms
from .models import ShopInfo

class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopInfo
        fields = '__all__'
