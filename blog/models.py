from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
