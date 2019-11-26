from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.FilePathField('/img')
    technology = models.TextField()
