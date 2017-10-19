from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Typeinfo)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Goodsinfo)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gprice', 'gunit', 'grepertory','gclick','gtype']
    list_per_page = 10
    search_fields = ('gtitle','gcontent')