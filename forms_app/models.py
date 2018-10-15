from django.db import models
from datetime import datetime


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=500)
    timeCook = models.IntegerField()
    dateCreated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + self.recipe + (str(self.timeCook))