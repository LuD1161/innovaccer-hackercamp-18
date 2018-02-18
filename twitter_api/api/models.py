from django.db import models


# Create your models here.

class Tweets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    timestamp_ms = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=280)
    geo = models.CharField(max_length=50, blank=True, null=True)
    coordinates = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    in_reply_to_screen_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('User', related_name='user')


class User(models.Model):
    # User details
    _id = models.CharField(max_length=20)
    created_at = models.CharField(max_length=150)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    lang = models.CharField(max_length=5)
    profile_image_url = models.URLField()
    name = models.CharField(max_length=40)
    screen_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    verified = models.BooleanField()
    protected = models.BooleanField()
    followers_count = models.IntegerField()
    status_count = models.IntegerField()
