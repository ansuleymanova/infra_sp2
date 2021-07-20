
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (TitleViewSet,
                    GenreViewSet,
                    CategoryViewSet)


v1_router = DefaultRouter()
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('v1/', include(v1_router.urls)), ]
