'''
__author__      =       "Roberto Rocuant"
__version__     =       "0.1"
__created__     =       "05-08-2019-08:51"
'''


from league.settings import DEBUG
from datetime import timedelta
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from requirements.version import version
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_401_UNAUTHORIZED,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from rest_framework.views import APIView


import json
import time


class LeagueLogin(APIView):

	permission_classes = (AllowAny,)


	@csrf_exempt
	def post(self, request):

		# Get credentials on request.
		username = request.data.get("username")
		password = request.data.get("password")

		# If username/password is not provide or the key is invalid. (one/both)
		if username is None or password is None or username == "" or password == "":
			return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)

		# Run the authentication.
		user = authenticate(username=username, password=password)
		
		if not user:
			return Response({'error': 'Invalid credentials.'}, status=HTTP_404_NOT_FOUND)

		# Refresh token. (in every login)
		Token.objects.filter(user=user).delete()		
		token, _ = Token.objects.get_or_create(user=user)

		return Response({'token': token.key}, status=HTTP_200_OK)


class LeagueOfLegends(APIView):

	permission_classes = (AllowAny,)
	@csrf_exempt
	def get(self, request):

		# Get request data.
		form = request.data
		a = form['abc']
		result = {
			'asd': a,
			'dsa': 2,
		}
		return Response(result, status=HTTP_200_OK)