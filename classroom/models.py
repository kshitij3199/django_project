from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return  self.artist


