'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''


from .views import (
    Home, 
    LeagueProfile, 
    LeagueRanked,
    ProfileAPI,
)
from django.urls import path


urlpatterns = [
	path(
        '',
        Home.as_view(),
        name = "home",
    ),	
	path(
        'profile/',
        LeagueProfile.as_view(),
        name = "profile",
    ),
    path(
        'profile-api/',
        ProfileAPI.as_view(),
        name = "profileapi",
    ),  
    path(
        'ranked/',
        LeagueRanked.as_view(),
        name = "ranked",
    ),
]