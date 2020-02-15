from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'venues', views.VenueViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('', include(router.urls)),
]
