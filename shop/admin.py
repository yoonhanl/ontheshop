from django.contrib import admin
from .models import *
# Register your models here.

class CagegoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'avaliable_display',
    'avaliable_order', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price', 'stock', 'avaliable_display', 'avaliable_order']


admin.site.register(Category, CagegoryAdmin)
admin.site.register(Product, ProductAdmin)
