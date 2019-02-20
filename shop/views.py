from django.shortcuts import render
from .models import ShopInfo

# Create your views here.
def index(request):
    # 전체 shop 목록을 가져올 예정이다.
    qs = ShopInfo.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list':qs, 
    })

def shop_detail(request, pk):
    shop = ShopInfo.objects.get(pk=pk) # 즉시 DB에서 가져옴
    return render(request, 'shop/shop_detail.html', {
        'shop':shop,
    })
