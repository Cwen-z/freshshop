from django.contrib import admin
from .models import Carinfo
# Register your models here.


@admin.register(Carinfo)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','goods','counts']
    list_per_page = 10