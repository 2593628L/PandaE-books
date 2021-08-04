from typing import ChainMap

from django.db import models
from django.db.models.fields import CharField, Field
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    MAX_LENGTH = 200
    name = models.CharField(max_length=MAX_LENGTH,unique=True)
    likes = models.IntegerField(default=0)
    Sdescription =models.CharField(max_length=MAX_LENGTH)
    slug = models.SlugField(unique=True,blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name



class Book(models.Model):
    TITLE_MAX_SIZE = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=TITLE_MAX_SIZE)
    slug = models.SlugField(unique=True,blank=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='book_images',blank = True)
    likes = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    description = models.CharField(max_length=500)
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/book_images/rango.jpg'

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images',blank = True)

    def __str__(self):
        return self.user.username

class Favorites(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)

class Comments(models.Model):
    MAX_SIZE = 128
    type = models.CharField(max_length=MAX_SIZE)
    Date = models.DateField()
    Rate = models.PositiveSmallIntegerField()
    content = CharField(max_length=128)
    user = models.ManyToManyField(User)
    book = models.ManyToManyField(Book)