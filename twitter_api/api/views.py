import time

from django.shortcuts import redirect
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, DjangoFilterBackend
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API
from twitter_api.settings import consumer_key, consumer_secret, access_token_secret, access_token
from rest_framework import viewsets, mixins

from .filters import UserFilter, TweetFilter
from .serializers import (
    UserSerializer,
    TweetSerializer)
from .pagination import LimitTenPagination
from .models import Tweets, User

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)


# Not used upto nows
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


@api_view(['GET'])
def get_track(request):
    query = request.GET.get('q')
    results = api.search(q=query)
    final = []
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
    return redirect('/api/tweets/?text=&text__icontains=' + query)


class TweetViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = TweetSerializer
    queryset = Tweets.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = LimitTenPagination
    filter_class = TweetFilter


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = LimitTenPagination
    filter_class = UserFilter
