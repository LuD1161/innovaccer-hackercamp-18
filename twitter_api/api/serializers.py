from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Tweets, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='users-detail',
        queryset=User.objects.all()
    )
    username = SerializerMethodField()

    def get_username(self, obj):
        # print(type(obj))
        return obj.user.name

    class Meta:
        model = Tweets
        fields = "__all__"
