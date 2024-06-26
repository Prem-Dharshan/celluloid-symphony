from django.urls import path
from .views import *

urlpatterns = [

    # SEARCH
    path('search-movie/<str:movie_name>',
         MovieSearchView.as_view(), name='search-movie'),
    path('search-tv-show/<str:tv_show_name>',
         TVShowSearchView.as_view(), name='search-tv-show'),
    path('search-all/<str:content_name>',
         MultiSearchView.as_view(), name='search-all'),

    # DETAIL
    path('movie-detail/<int:movie_id>',
         MovieDetailView.as_view(), name='movie-detail'),

    # MOVIE LISTS
    path('now-playing', NowPlayingView.as_view(), name='now-playing'),

    # TRENDING
    path('trending/all', TrendingView.as_view(), name='trending-all'),

    # IMAGES
    path('images/<str:content_type>/<int:content_id>',
         ImageView.as_view(), name='images'),
    # 577922
    # 70523
]
