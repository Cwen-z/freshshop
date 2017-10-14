from django.contrib import admin
from .models import *
# Register your models here.
class Addressinline(admin.TabularInline):
    model = Addressinfo
    extra = 2

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['uname','uemail','uphone']
    inlines = [Addressinline]