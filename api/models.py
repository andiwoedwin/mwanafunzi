from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.dispatch import receiver


# class User(AbstractUser):
#     USER_ROLES = (
#         ('CA', 'COMPANY ADMIN'),
#         ('NU', 'NORMAL USER')
#     )
#     role = models.CharField(
#         verbose_name='user role', max_length=2, choices=USER_ROLES,default='NU'
#     )

CATEGORY_CHOICES = (
    ("snacks", "snacks"),
    ("Toiletaries", "Toiletaries"),
    ("Books", "Books"),
    ("Stationery", "Stationery"),
    ("Books", "Books"),
)


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = CloudinaryField('image')
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)




