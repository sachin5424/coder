from django.contrib import admin
from .models import Item,Categories
# Register your models here.


@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    list_display = ['id','Categories_name']

@admin.register(Item)
class Categories_admin(admin.ModelAdmin):
    list_display = ['id','Item_categories','Item_title','is_Active','is_Featured']


