from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('Genre',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)

    def __str__(self):
        return f'{self.name}'