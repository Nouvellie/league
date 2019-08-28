'''
__author__      =       "Roberto Rocuant"
__version__     =       "0.10"
__created__     =       "27-08-2019-23:30"
'''


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	
	# Admin:
    path('admin/', admin.site.urls),

    # Apps:
    path('', include('apps.core.urls')),

    # Main:

]
