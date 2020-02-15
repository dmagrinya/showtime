from django.db import models

class Venue(models.Model):
    """Model representing a venue."""

    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""

        return self.name



class Artist(models.Model):
    """Model representing an artist."""

    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='artists', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""

        return self.name



class Show(models.Model):
    """Model representing a show."""

    name = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE) 
    artists = models.ManyToManyField(Artist) 
    kick_off = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['kick_off']

    def __str__(self):
        """String for representing the Model object."""

        return self.name



