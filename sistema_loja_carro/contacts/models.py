from django.db import models
from datetime import datetime

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    custumer_need = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True, default=datetime.now)

    def __str__(self):
        return self.email



