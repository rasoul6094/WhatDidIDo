from django.contrib import admin
from .models import MainCategory, SubCategory,Activity
# Register your models here.

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Activity)
