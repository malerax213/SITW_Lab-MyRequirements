"""
WSGI config for myrecommendations project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
>>>>>>> 314c1e3cfd5a2a31dc8fb54eb7c4bce031b4f13f
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myrecommendations.settings")

application = get_wsgi_application()
