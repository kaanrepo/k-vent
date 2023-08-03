from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


# Register your models here.

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    model = User
    list_display = ('username', 'email', 'staff')
    list_filter = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('staff', 'superuser', 'active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    filter_horizontal = ()
    search_fields = ('username', 'email')


admin.site.register(User, CustomUserAdmin)
