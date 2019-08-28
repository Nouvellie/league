'''
__author__      =       "Roberto Rocuant"
__version__     =       "0.10"
__created__     =       "27-08-2019-23:30"
'''


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'league.settings')

application = get_wsgi_application()
