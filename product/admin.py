from atexit import register
from django.contrib import admin
from .models import BC


# Register your models here.
@admin.register(BC)
class barcodeadmin(admin.ModelAdmin):
    list_display=['id','name','bcode']