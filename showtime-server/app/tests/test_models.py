from django.test import TestCase
from app.models import Venue, Artist, Show
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class VenueModelTest(TestCase):
    VenueUT = None

    @classmethod
    def setUpTestData(cls):
        Venue.objects.create(name='Queimada')

    def setUp(self):
        self.VenueUT = Venue.objects.get(name='Queimada')

    def test_name_label(self):
        field_label = self.VenueUT._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.VenueUT._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        self.assertEquals('Queimada', str(self.VenueUT))



class ArtistModelTest(TestCase):
    ArtistUT = None

    @classmethod
    def setUpTestData(cls):
        manager_password = make_password('password')
        artist_owner = User.objects.create(username="Artist Manager", password=manager_password)
        Artist.objects.create(name='James Hunter', owner=artist_owner)

    def setUp(self):
        self.ArtistUT = Artist.objects.get(name='James Hunter')

    def test_name_label(self):
        field_label = self.ArtistUT._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.ArtistUT._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_owner_label(self):
        field_label = self.ArtistUT._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_owner_class(self):
        class_name = self.ArtistUT._meta.get_field('owner').related_model.__name__
        self.assertEquals(class_name, 'User')

    def test_owner_many_to_one(self):
        field_is_many_to_one = self.ArtistUT._meta.get_field('owner').many_to_one
        self.assertTrue(field_is_many_to_one)

    def test_owner_on_delete(self):
        artist_owner = User.objects.get(username='Artist Manager')
        artist_owner.delete()
        self.assertEquals(Artist.objects.count(), 0)

    def test_object_name(self):
        self.assertEquals('James Hunter', str(self.ArtistUT))



class ShowModelTest(TestCase):
    ArtistUT = None

    @classmethod
    def setUpTestData(cls):
        show_venue = Venue.objects.create(name='Queimada')
        Show.objects.create(name='R&B Show', venue=show_venue)

    def setUp(self):
        self.ShowUT = Show.objects.get(name='R&B Show')

    def test_name_label(self):
        field_label = self.ShowUT._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.ShowUT._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_venue_label(self):
        field_label = self.ShowUT._meta.get_field('venue').verbose_name
        self.assertEquals(field_label, 'venue')

    def test_venue_class(self):
        class_name = self.ShowUT._meta.get_field('venue').related_model.__name__
        self.assertEquals(class_name, 'Venue')

    def test_venue_on_delete(self):
        show_venue = Venue.objects.get(name='Queimada')
        show_venue.delete()
        self.assertEquals(Show.objects.count(), 0)

    def test_artists_label(self):
        field_label = self.ShowUT._meta.get_field('artists').verbose_name
        self.assertEquals(field_label, 'artists')

    def test_artists_class(self):
        class_name = self.ShowUT._meta.get_field('artists').related_model.__name__
        self.assertEquals(class_name, 'Artist')

    def test_artists_many_to_many(self):
        field_is_many_to_many = self.ShowUT._meta.get_field('artists').many_to_many
        self.assertTrue(field_is_many_to_many)

    def test_kick_off_label(self):
        field_label = self.ShowUT._meta.get_field('kick_off').verbose_name
        self.assertEquals(field_label, 'kick off')

    def test_kick_off_blank(self):
        field_can_be_blank = self.ShowUT._meta.get_field('kick_off').blank
        self.assertTrue(field_can_be_blank)

    def test_kick_off_null(self):
        field_can_be_null = self.ShowUT._meta.get_field('kick_off').null
        self.assertTrue(field_can_be_null)

    def test_ordering(self):
        self.assertEquals(self.ShowUT._meta.ordering, ['kick_off'])

    def test_object_name(self):
        self.assertEquals('R&B Show', str(self.ShowUT))
