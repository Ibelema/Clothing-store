from django.contrib import admin
from apps.accounts.models import User
from django.utils.translation import gettext_lazy as _

#to customise the admin page
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "is_email_verified", "created_at")
    list_filter = list_display
    #this is to separte fieldss
    fieldsets = (
        (
            _("Login credentials"),
            {"fields": ("email", "password")}
       ),
       (
            _("Personal Information"),
            {"fields": ("first_name", "last_name", "avatar")}
       ),
       (
            _("Permissions and Groups"),
            {"fields":("is_email_verified", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}
       ),
       (
            _("Important Dates"),
            {"fields": ("created_at", "updated_at", "last_login")}
       ),
    )

    readonly_fields = ("created_at", "updated_at")

admin.site.register(User, UserAdmin)