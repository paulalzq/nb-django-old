import os, sys

# edit your username below
sys.path.append("/home/paulalzq/public_html")

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'nobinarix.settings'

application = get_wsgi_application()