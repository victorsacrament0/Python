from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Perfil(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='img_perfil')
    class Meta:
        verbose_name = 'Perfi'

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)                      #diminuindo o tamanho das imagens para salvar, pra ficar mais leve
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
