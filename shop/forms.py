from django import forms
from .models import ShopInfo

class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopInfo
        # fields = '__all__'  # 모든 필드 가져오기
        fields = ['name', 'desc', 'address']  # 지정 필드만 가져오기 ('photo')
