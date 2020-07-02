import os, sys

sys.path.append("/home/paulalzq/public_html");
os.environ['DJANGO_SETTINGS_MODULE'] = 'nb.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/paulalzq/.python_egg_cache'
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)

# sys.path.append("/home/paulalzq/public_html/nb/nb")

# from django.core.wsgi import get_wsgi_application

# os.environ['DJANGO_SETTINGS_MODULE'] = 'nb.settings'

# application = get_wsgi_application()