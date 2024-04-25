from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class CustomUser(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def __str__(self):
        return self.username

CustomUser = get_user_model()

class Chef(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    background = models.TextField()
    specialty = models.CharField(max_length=150)

    class Meta:
        db_table = "Chefs"

class Ingredient(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Ingerients"

class Dish(models.Model):
    chef = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    tutorial = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='dishes') 

    class Meta:
        db_table = "Dishes"

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    class Meta:
        db_table = "Ratings"