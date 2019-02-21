from django.shortcuts import render, redirect
from .models import ShopInfo
from .forms import ShopForm

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

def shop_new(request):
    form_cls = ShopForm

    if request.method == "POST":
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save()
            return redirect('/shop/{}/' .format(shop.id))
    else:
        form = form_cls()

    return render(request, 'shop/shop_form.html', {
        'form' : form,
    })

from django.views.generic import CreateView

shop_new_cbv = CreateView.as_view(
    model=ShopInfo, form_class=ShopForm,
    template_name='shop/shop_form.html',
    success_url='/shop/')
