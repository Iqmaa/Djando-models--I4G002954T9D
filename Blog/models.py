from cgitb import text
from pydoc import describe
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    author = models.ForeignKey(settings.get_user_model())
    created_date = models.DateTimeField(auto_new_add=True)
    Published_date = models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return self.title
