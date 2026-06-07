from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, unique=True, error_messages={'unique': "Já existe um registro com este valor. Duplicatas não são permitidas!"})
    age = models.IntegerField()