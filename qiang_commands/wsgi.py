"""
WSGI config for qiang_commands project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qiang_commands.settings")

application = Cling(get_wsgi_application())
