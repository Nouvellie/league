'''
__author__      =       "Roberto Rocuant"
__version__     =       "1.0.0"
__created__     =       "03/23/2020 02:53"
'''

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    # Main app. 
    path(
        '',
        include('apps.core.urls'),
    ), 
] + static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )