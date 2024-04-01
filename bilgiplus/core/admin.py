from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser, Interest

# Register your models here.
@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    list_display = ('username','email','interests')

admin.site.register(Interest)