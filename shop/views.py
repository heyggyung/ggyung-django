from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .models import ShopInfo
from .forms import ShopForm


# Create your views here.
# def index(request):
#     # 전체 shop 목록을 가져올 예정이다.
#     qs = ShopInfo.objects.all()
#     return render(request, 'shop/shop_list.html', {
#         'shop_list':qs,
#     })

# index = PostListView.as_view()

# class PostListView(ListView):
#     model = ShopInfo

#     def get_context_data(self):
#         context = super().get_context_data()
#         context.update({
#             'hello': 'world',
#         })
#         return context

# def shop_detail(request, pk):
#     shop = ShopInfo.objects.get(pk=pk) # 즉시 DB에서 가져옴
#     return render(request, 'shop/shop_detail.html', {
#         'shop':shop,
#     })

@login_required
def shop_new(request):
    form_cls = ShopForm

    if request.method == "POST":
        form = form_cls(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.save()
            return redirect(shop)
    else:
        form = form_cls()

    return render(request, 'shop/shop_form.html', {
        'form' : form,
    })

@login_required
def shop_edit(request, pk):
#    shop = ShopInfo.objects.get(pk=pk)
    shop = get_object_or_404(ShopInfo, pk=pk)
  
    if request.user != shop.user:
        return redirect(shop)

    form_cls = ShopForm

    if request.method == "POST":
        form = form_cls(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save()
            return redirect('/shop/{}/' .format(shop.id))
    else:
        form = form_cls(instance=shop)

    return render(request, 'shop/shop_form.html', {
        'form' : form,
    })

@login_required
def shop_delete(request, pk):
    shop = get_object_or_404(ShopInfo, pk=pk)
  
    if request.user != shop.user:
        return redirect(shop)

    if request.method == 'POST':
        shop.delete()
        return redirect('shop:index')

    return render(request, 'shop/shop_confirm_delete.html', {
        'shop': ShopInfo,
    })


# 클래스 기반으로 view, detail 함수 구현
index = ListView.as_view(model=ShopInfo,
                         context_object_name='shop_list',
                         template_name='shop/shop_list.html')

shop_detail = DetailView.as_view(model=ShopInfo,
                         context_object_name='shop',
                         template_name='shop/shop_detail.html')

# shop_delete = DeleteView.as_view(model=ShopInfo,
#                          context_object_name='shop',
#                          template_name='shop/shop_confirm_delete.html',
#                          success_url=reverse_lazy('shop:index'))

# 클래스 기반으로 new, edit 함수 구현
shop_new_cbv = CreateView.as_view(
    model=ShopInfo, form_class=ShopForm, template_name='shop/shop_form.html')

shop_edit_cbv = UpdateView.as_view(
    model=ShopInfo, form_class=ShopForm, template_name='shop/shop_form.html')
