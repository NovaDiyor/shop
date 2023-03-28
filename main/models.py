from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=210)
    image = models.ImageField(upload_to='product/')
    text = models.TextField()
    price = models.CharField(max_length=210)


class Wishlist(models.Model):
    product = models.ManyToManyField(Product)


class User(AbstractUser):
    security = models.CharField(max_length=210)
    sex = models.IntegerField(choices=(
        (1, 'male'),
        (2, 'female')
    ))
