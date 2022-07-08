from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth import get_user_model

from .forms import UserChangeForm, SignupForm


class UserAdmin(DefaultUserAdmin):
    model = get_user_model()
    form = UserChangeForm
    add_form = SignupForm
    list_display = ['name', 'email']
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        (None, {'fields': ('name',)}),
    )


admin.site.register(get_user_model(), UserAdmin)
