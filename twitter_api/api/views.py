import time

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from twitter_api.settings import consumer_key, consumer_secret, access_token_secret, access_token

from rest_framework import viewsets, mixins

from .filters import Filter_followers_count
from .serializers import (
    UserSerializer,
    TweetSerializer)
from .pagination import LimitTenPagination

from .models import Tweets, User

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)


class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            return raw_data
            # return True
        except BaseException as e:
            print(e)
            time.sleep(10)

    def on_error(self, status_code):
        print status_code

# Not used upto now
twitterStream = Stream(auth=auth, listener=listener())


def get_track(request):
    query = request.GET.get('q')
    results = api.search(q=query)
    final = []
    """
    keys 
    contributors
    truncated
    text
    is_quote_status
    in_reply_to_status_id
    id
    favorite_count
    entities
    quoted_status_id
    retweeted
    coordinates
    source
    in_reply_to_screen_name
    in_reply_to_user_id
    retweet_count
    id_str
    favorited
    retweeted_status
    user
    geo
    in_reply_to_user_id_str
    lang
    created_at
    quoted_status_id_str
    in_reply_to_status_id_str
    place
    metadata
    
    timestamp_ms = models.DateTimeField(default=None)
    text = models.CharField(max_length=280)
    geo = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    in_reply_to_screen_name = models.CharField(max_length=50)
    user = models.ForeignKey('User', 
    
    _id = models.CharField(max_length=20)
    created_at = models.CharField(max_length=150)
    timezone = models.CharField(max_length=100)
    lang = models.CharField(max_length=5)
    profile_image_url = models.URLField()
    name = models.CharField(max_length=40)
    screen_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    url = models.CharField(max_length=200)
    verified = models.BooleanField()
    protected = models.BooleanField()
    followers_count = models.IntegerField()
    status_count = models.IntegerField()
    """
    for result in results:
        j_data = result._json
        data = j_data
        user_d = data['user']
        try:
            user = User.objects.get(_id=user_d['id'])
            if user:
                pass
        except User.DoesNotExist:
            user = User.objects.create(_id=user_d['id'],
                                       created_at=user_d['created_at'],
                                       timezone=user_d['time_zone'],
                                       lang=user_d['lang'],
                                       profile_image_url=user_d['profile_image_url'],
                                       name=user_d['name'],
                                       screen_name=user_d['screen_name'],
                                       location=user_d['location'],
                                       url=user_d['url'],
                                       verified=user_d['verified'],
                                       protected=user_d['protected'],
                                       followers_count=user_d['followers_count'],
                                       status_count=user_d['statuses_count'])
        try:
            tweet = Tweets.objects.get(id=data['id'])
            if user:
                pass
        except Tweets.DoesNotExist:
            tweet_obj = Tweets.objects.create(id=data['id'],
                                              text=data['text'],
                                              geo=data['geo'],
                                              coordinates=data['coordinates'],
                                              place=data['place'],
                                              in_reply_to_screen_name=data['in_reply_to_screen_name'],
                                              user=user)
        final.append(j_data)
    return HttpResponse(final)


class TweetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TweetSerializer
    queryset = Tweets.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('text', 'place', 'user')
    pagination_class = LimitTenPagination
    search_fields = ('text', 'place', 'user')


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'screen_name', 'location')
    pagination_class = LimitTenPagination
    search_fields = ('name', 'screen_name', 'location')
