from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'venues', views.VenueViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls)),
]
