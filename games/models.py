from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    release_year = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.title} ({self.release_year}) - Rating: {self.rating}"