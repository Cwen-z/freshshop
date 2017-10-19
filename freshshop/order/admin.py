from django.contrib import admin
from .models import *
# Register your models here.

class DetailInline(admin.TabularInline):
    model = Orderdetail
    extra = 10


@admin.register(Orderinfo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['oid','ouser','odate','ototal','opay','ostate','oaddress']
    inlines = [DetailInline]
    list_per_page = 10
    search_fields = ('ouser__uname','oid','odate')
