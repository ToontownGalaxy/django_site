from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Key(models.Model):
    key = models.CharField(max_length=16, blank=False, null=False)