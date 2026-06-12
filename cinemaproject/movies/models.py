from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title