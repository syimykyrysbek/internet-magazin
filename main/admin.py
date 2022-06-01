from django.contrib import admin
from main.models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # list_display = ['adress', 'number', 'message']
    # search_fields = ['adress', 'number', 'message']
    # list_editable = ['number']
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
