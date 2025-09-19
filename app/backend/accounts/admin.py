from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "age", "gender", "is_staff", "is_superuser")
    search_fields = ("email", "username")
    list_filter = ("is_staff", "is_superuser", "gender")
    ordering = ("id",)
    