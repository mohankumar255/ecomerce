from django.contrib import admin
from .models import items,types,save_order
# Register your models here.
admin.site.register(items)
admin.site.register(types)
admin.site.register(save_order)