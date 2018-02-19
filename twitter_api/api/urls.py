from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TweetViewSet, UserViewSet
from . import views

tweet_list = TweetViewSet.as_view({
    'get': 'list'
})

tweet_detail = TweetViewSet.as_view({
    'get': 'retrieve'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()

router.register(r'tweets', views.TweetViewSet, base_name='tweets')
router.register(r'users', views.UserViewSet, base_name='users')

urlpatterns = [
    url(r'^query/$', views.get_track, name='query'),
    url(r'^', include(router.urls))
]