'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''


from leaguestats.settings import API_KEY
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK, 
	HTTP_400_BAD_REQUEST, 
	HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView


import re
import requests
import traceback


class Home(TemplateView):

	template_name = 'core/home.html'

class LeagueProfile(TemplateView):

	template_name = 'core/profile.html'

class LeagueRanked(TemplateView):

	template_name = 'core/ranked.html'


class ProfileAPI(APIView):

	permission_classes = (AllowAny,)

	def post(self, request):

		form = request.data

		nick = form['nick']

		try:
			url = 'https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + str(nick)
			params = {
				'api_key': API_KEY,
			}
			api_call = requests.get(url=url, params=params,).json()

			return Response(api_call, status=HTTP_200_OK)

		except Exception as e:
			errors = {
				'error': str(e),
				'traceback': re.sub(r"\n\s*", " || ", traceback.format_exc()),
			}

			return Response(errors, status=HTTP_400_BAD_REQUEST)





