from django.contrib import admin
from .models import Category, Product, User, News


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(News)
admin.site.register(User)