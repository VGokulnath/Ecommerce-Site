from django.contrib import admin
from .models import Products,Order

# Register your models here.
admin.site.site_header = "Ecoomerce Site"
admin.site.site_title = "Ecom site"

class ProductAdmin(admin.ModelAdmin):
    def change_catogory_to_default(self,request,queryset):
        queryset.update(catogory="default")


    list_display = ('title','price','discount_price','catogory','image')
    search_fields = ('title',)
    actions = ('change_catogory_to_default',)
    list_editable = ('discount_price',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)