from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='img_perfil')
    class Meta:
        verbose_name = 'Perfi'

    def __str__(self):
        return f'Perfil de {self.user.username}'
