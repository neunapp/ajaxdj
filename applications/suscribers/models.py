from django.db import models

# Create your models here.
class Suscriptor(models.Model):
    full_name = models.CharField(
        'Nombres',
        max_length=50
    )
    email = models.EmailField()

    def __str__(self):
        return self.full_name