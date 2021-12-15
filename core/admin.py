from django.contrib import admin

# Register your models here.
from core.models import Category, Item, Customer

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Customer)
