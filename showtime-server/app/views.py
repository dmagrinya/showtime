from rest_framework import viewsets
from app.models import Venue, Artist
from django.contrib.auth.models import User
from app.serializers import VenueSerializer, ArtistSerializer, UserSerializer
from app.permissions import IsOwnerOrReadOnly



class VenueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """

    queryset = Venue.objects.all()
    serializer_class = VenueSerializer



class ArtistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
