from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")

    fieldsets = (
        ("Personal info", {"fields": ("username", "email", "first_name", "last_name", "gender")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email","gender", "password1", "password2"),
            },
        ),
    )


User = get_user_model()

admin.site.register(User, MyUserAdmin)