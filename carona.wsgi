import os
import sys	
import site
site.addsitedir('/home/lucas/public/nossacarona.com.br/env/lib/python2.7/site-packages')
sys.path.append('/home/lucas/public/nossacarona.com.br/public/NossaCarona/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'NossaCarona.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
