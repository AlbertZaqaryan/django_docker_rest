from django.contrib import admin
from .models import Car, Book, Notebook
# Register your models here.

admin.site.register(Car)
admin.site.register(Book)
admin.site.register(Notebook)