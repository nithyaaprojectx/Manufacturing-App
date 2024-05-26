# manufacturer/models.py

from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
