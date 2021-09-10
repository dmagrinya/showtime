from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Venue, Artist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class VenueTest(APITestCase):
    def test_create_venue_unauthenticated(self):
        """
        Ensure unauthenticated user can create a new venue object.
        """

        url = reverse('venue-list')
        data = {'name': 'Queimada'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venue.objects.count(), 1)
        self.assertEqual(Venue.objects.get().name, 'Queimada')



class ArtistTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        encrypted_password = make_password('password')
        user = User.objects.create(username='manager', password=encrypted_password)
        import pdb; pdb.set_trace()
        User.objects.create(username='eve', password=encrypted_password)

    def test_create_artist_authenticated(self):
        """
        Ensure we can create a new artist object.
        """
        loggedin = self.client.login(username='manager', password='password')

        """
        WIP:
        token = User.objects.get(username='manager').oauth2_provider_accesstoken.create(expires='2020-05-31 23:15', token='fasdfasd748')
        self.client.credentials(Authorization='Bearer {}'.format(token))
        """

        url = reverse('artist-list')
        data = {'name': 'James Hunter'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(Artist.objects.get().name, 'James Hunter')
        self.assertEqual(Artist.objects.get().owner.username, 'manager')

    def test_forbidden_create_artist_unauthenticated(self):
        """
        Ensure create artist is forbidden for an unauthenticated user
        """

        url = reverse('artist-list')
        data = {'name': 'James Hunter'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_artist_owned(self):
        """
        Ensure user owning artist can modify it
        """
        self.client.login(username='manager', password='password')

        url = reverse('artist-list')
        data = {'name': 'James Hunter'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('artist-detail', args=[4])
        data = {'name': 'James Hunter Modified'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.get().name, 'James Hunter Modified')
        self.assertEqual(Artist.objects.get().owner.username, 'manager')

    def test_forbidden_modify_artist_not_owned(self):
        """
        Ensure user not owning artist cannot modify it
        """
        self.client.login(username='manager', password='password')

        url = reverse('artist-list')
        data = {'name': 'James Hunter'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.logout()
        self.client.login(username='eve', password='password')

        url = reverse('artist-detail', args=[3])
        data = {'name': 'James Hunter Modified'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
