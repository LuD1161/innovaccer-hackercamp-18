from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PageTenPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class LimitTenPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'     # default value
    offset_query_param = 'offset'   # default value
    max_limit = 100
