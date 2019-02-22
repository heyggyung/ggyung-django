from django.contrib import admin
from .models import ShopInfo, Item

# Register your models here.
@admin.register(ShopInfo)
class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'created_at', 'user']
    list_display_links = ['name']



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_public', 'price']
    list_display_links = ['name']

# admin.site.register(Comment)
