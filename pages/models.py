from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    desgination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    facebook_link = models.URLField(max_length=95)
    twiter_link = models.URLField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    google_plus_link = models.URLField(max_length=85)