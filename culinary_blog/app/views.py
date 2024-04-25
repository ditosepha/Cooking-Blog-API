from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, HttpResponse
from .permissions import IsChefOrReadOnly
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DishFilter

@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class dishesViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsChefOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilter

class ChefViewSet(ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerilizer
    permission_classes = [permissions.IsAdminUser]

class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]



