from django.contrib import admin

# Register your models here.
from .models import Aluno,Campus

admin.site.register(Aluno),
admin.site.register(Campus)