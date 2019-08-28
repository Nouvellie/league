'''
__author__      =       "Roberto Rocuant"
__version__     =       "0.1"
__created__     =       "05-08-2019-08:51"
'''


from .views import LeagueLogin, LeagueOfLegends
from django.urls import path


urlpatterns = [

	# User:
    path('login', 		LeagueLogin.as_view(),			name='login'),

    # Main:
    path('', 			LeagueOfLegends.as_view(),			name='main'),
]