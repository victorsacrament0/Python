from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth
from .form import UserChangeForm, UserCreationForm


@admin.register(Users)
class UserAdmin(admin_auth.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth.UserAdmin.fieldsets + (
        ('Cargo', {'fields':('cargo',)}),
    )