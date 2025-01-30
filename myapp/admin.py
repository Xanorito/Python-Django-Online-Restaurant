from django.contrib import admin
from django.utils.html import format_html
from . models import Category, Item, Order

# Register your models here.
@admin.register(Category)
class AdminCate(admin.ModelAdmin):
    list_display=('cat_id','cat_name')

@admin.register(Item)
class AdminCate(admin.ModelAdmin):
    def prodimg(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    list_display=('name','category','desc','price','prodimg')

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display=('user', 'product', 'quantity', 'date_ordered', 'payment_status', 'address')