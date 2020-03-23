'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''


from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):

	template_name = 'core/home.html'

class LeagueProfile(TemplateView):

	template_name = 'core/profile.html'

class LeagueRanked(TemplateView):

	template_name = 'core/ranked.html'