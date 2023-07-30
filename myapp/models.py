from django.db import models

# Create your models here.


class products(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    info = models.TextField()
    img = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name
