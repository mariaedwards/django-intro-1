"""Django models
"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    """Movie model
    """
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2100),
            MinValueValidator(1900)
        ]
    )
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}: {self.release_year}'
