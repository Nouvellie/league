'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''


from leaguestats.settings import API_KEY
from django.shortcuts import render
from django.views.generic import TemplateView
from math import floor
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK, 
	HTTP_400_BAD_REQUEST, 
	HTTP_403_FORBIDDEN,
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
		region = form['region'] # LAN, LAS, NA, EUW.

		try:
			summoner_url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + str(nick)
			params = {
				'api_key': API_KEY,
			}
			summoner_result = requests.get(url=summoner_url, params=params,)
			
			if summoner_result.status_code == 403:
				return Response({'error': 'Riot Api expired.'}, status=HTTP_403_FORBIDDEN)

			else: 
				summoner_result = summoner_result.json()

			summary_url = 'https://' + region + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summoner_result['id']

			summary_result = requests.get(url=summary_url, params=params,).json()

			final_summary = {}

			if len(summary_result) == 2:

				# Saving solo_q and flex result.
				if summary_result[0]['queueType'] == 'RANKED_SOLO_5x5':
					final_summary['solo_q'] = summary_result[0]
					final_summary['flex'] = summary_result[1]

				else:
					final_summary['solo_q'] = summary_result[1]
					final_summary['flex'] = summary_result[0]

				# Saving solo_q win ratio.
				if final_summary['solo_q']['wins'] == 0 and final_summary['solo_q']['losses'] == 0:
					solo_q_wr = 0

				elif final_summary['solo_q']['wins'] > 0 and final_summary['solo_q']['losses'] == 0:
					solo_q_wr = 100

				else:
					solo_q_wr = floor(final_summary['solo_q']['wins'] / (final_summary['solo_q']['wins'] + final_summary['solo_q']['losses']) * 100)

				final_summary['solo_q'].update({
					'solo_q_wr': solo_q_wr,
					'solo_q_tierIcon': '/media/rank-icon/' + str(final_summary['solo_q']['tier']) + str(final_summary['solo_q']['rank']) + '.png',
				})

				# Saving flex win ratio.
				if final_summary['flex']['wins'] == 0 and final_summary['flex']['losses'] == 0:
					flex_wr = 0

				elif final_summary['flex']['wins'] > 0 and final_summary['flex']['losses'] == 0:
					flex_wr = 100

				else:
					flex_wr = floor(final_summary['flex']['wins'] / (final_summary['flex']['wins'] + final_summary['flex']['losses']) * 100)

				final_summary['flex'].update({
					'flex_wr': flex_wr,
					'flex_tierIcon': '/media/rank-icon/' + str(final_summary['flex']['tier']) + str(final_summary['flex']['rank']) + '.png',
				})

				# return Response(final_summary, status=HTTP_200_OK)
			
			elif len(summary_result) == 1:

				# Saving solo_q result and win ratio.
				if summary_result[0]['queueType'] == 'RANKED_SOLO_5x5':
					final_summary['solo_q'] = summary_result[0]

					if final_summary['solo_q']['wins'] == 0 and final_summary['solo_q']['losses'] == 0:
						solo_q_wr = 0

					elif final_summary['solo_q']['wins'] > 0 and final_summary['solo_q']['losses'] == 0:
						solo_q_wr = 100

					else:
						solo_q_wr = floor(final_summary['solo_q']['wins'] / (final_summary['solo_q']['wins'] + final_summary['solo_q']['losses']) * 100)

					final_summary['solo_q'].update({
						'solo_q_wr': solo_q_wr,
						'solo_q_tierIcon': '/media/rank-icon/' + str(final_summary['solo_q']['tier']) + str(final_summary['solo_q']['rank']) + '.png',
					})

				else:

					# Saving flex result and win ratio.
					final_summary['flex'] = summary_result[0]	

					if final_summary['flex']['wins'] == 0 and final_summary['flex']['losses'] == 0:
						flex_wr = 0

					elif final_summary['flex']['wins'] > 0 and final_summary['flex']['losses'] == 0:
						flex_wr = 100

					else:
						flex_wr = floor(final_summary['flex']['wins'] / (final_summary['flex']['wins'] + final_summary['flex']['losses']) * 100)

					final_summary['flex'].update({
						'flex_wr': flex_wr,
						'flex_tierIcon': '/media/rank-icon/' + str(final_summary['flex']['tier']) + str(final_summary['flex']['rank']) + '.png',
					})

				# return Response(final_summary, status=HTTP_200_OK)

			else:
				return Response({'error': 'No data found.'}, status=HTTP_404_NOT_FOUND)

			# Saving profile icon.
			extra = {
				'profileIcon': '/media/icon/'+ str(summoner_result['profileIconId']) +'.jpg',
			}	

			# Final response.
			final_response = {
				'summoner': summoner_result,
				'extra': extra,
			}

			if 'solo_q' in final_summary:
				final_response.update({
					'solo_q': final_summary['solo_q'],
					'solo_q_bool': True,
				})
			else:
				final_response.update({
					'solo_q_bool': False,
				})

			if 'flex' in final_summary:
				final_response.update({
					'flex': final_summary['flex'],
					'flex_bool': True,
				})
			else:
				final_response.update({
					'flex_bool': False,
				})

			return Response(final_response, status=HTTP_200_OK)

		except Exception as e:
			errors = {
				'error': str(e),
				'traceback': re.sub(r"\n\s*", " || ", traceback.format_exc()),
			}

			return Response(errors, status=HTTP_400_BAD_REQUEST)
