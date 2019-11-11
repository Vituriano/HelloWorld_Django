from django.contrib import admin
from .models import Gostos, Bio
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(Gostos)
admin.site.register(Bio, SingletonModelAdmin)