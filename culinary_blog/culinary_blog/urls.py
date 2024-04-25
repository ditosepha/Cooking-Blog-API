from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from app.views import *


router = DefaultRouter()
router.register(r'dishes', dishesViewSet)
router.register(r'chefs', ChefViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token)
]
