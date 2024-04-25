from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Dish)
admin.site.register(Chef)
admin.site.register(Rating)
admin.site.register(Ingredient)