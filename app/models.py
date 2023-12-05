from django.db import models

# Create your models here.

class Banda(models.Model):
    artist = models.CharField(max_length=200)
    release_date = models.DateField(null= True)
    price = models.DecimalField(decimal_places= True, max_digits=10000000)
    perfil = models.ImageField(upload_to='perfil/', null=True,verbose_name='Perfil')