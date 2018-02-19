from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework.fields import SerializerMethodField
from .models import Tweets, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = "__all__"
