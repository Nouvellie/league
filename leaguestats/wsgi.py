'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''


from django.core.wsgi import get_wsgi_application


import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leaguestats.settings')

application = get_wsgi_application()