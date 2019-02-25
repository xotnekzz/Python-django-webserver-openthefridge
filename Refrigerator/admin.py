from django.contrib import admin
from .models import Food, Shopping, Info, Recipe

# Register your models here.

admin.site.register(Food)
admin.site.register(Shopping)
admin.site.register(Recipe)
admin.site.register(Info)