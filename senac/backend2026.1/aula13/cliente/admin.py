from django.contrib import admin

# Register your models here.
from .models import Cliente,Conta

admin.site.register(Cliente)
admin.site.register(Conta)