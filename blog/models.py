from django.db import models

class Post(models.Model):
    username=models.CharField(max_length=255)
    description=models.TextField()
