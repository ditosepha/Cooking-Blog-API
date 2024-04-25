from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_superuser', 'is_staff', "is_active"]

class ChefSerilizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Chef
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ['user'] 
        extra_kwargs = {
            'user': {'default': serializers.CurrentUserDefault()}
        }
        permission_classes = [IsAuthenticated]

class DishSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), many=True, required=False)
    class Meta:
        model = Dish
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['chef'] = self.context['request'].user
        ingredients_data = validated_data.pop('ingredients', [])
        dish = Dish.objects.create(**validated_data)
        dish.ingredients.set(ingredients_data)
        return dish
    
    def update(slef, instance, validated_data):
        validated_data.pop('chef', None)
        instance = super().update(instance, validated_data)
        return instance