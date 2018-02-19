from django_filters.rest_framework import FilterSet
from .models import User, Tweets


class UserFilter(FilterSet):
    """
    Filter that allows greater than equal to the given no of followers
    """

    class Meta:
        model = User
        fields = {
            'name': ['exact', 'contains'],
            'screen_name': ['exact', 'contains'],
            'location': ['exact', 'contains'],
            'url': ['exact', 'contains'],
            'followers_count': ['gt', 'lt', 'exact']
        }


class TweetFilter(FilterSet):
    """
    Filter that allows greater than equal to the given no of followers
    """
    class Meta:
        model = Tweets
        fields = {
            'text': ['exact', 'icontains'],
            'place': ['exact', 'icontains'],
            'in_reply_to_screen_name': ['exact', 'icontains'],
            'id': ['exact', 'contains']
        }
