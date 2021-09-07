# This is Python code
print("Hello", "World")

def make_my_website():
    ...
    print("All done!")

#  config/settings.py
INSTALLED_APPS_type_list = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages', # new
]

# URL -> View -> Model -> Template


# pages/views.py
from django.http import HttpResponse

def homePageView( request ):
    return HttpResponse( 'Hello, World!' )


# pages/urls.py
from django.urls import path
try:
    from .views import homePageView
except ImportError:
    print( "homePageView is already available in this file" )

urlpatterns = [
    path( '', homePageView, name = 'home' )
]