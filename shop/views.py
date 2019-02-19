from django.shortcuts import render
from .models import ShopInfo

# Create your views here.
def index(request):
    # 전체 shop 목록을 가져올 예정이다.
    qs = ShopInfo.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list':qs, 
    })