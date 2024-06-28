"""
WSGI config for project2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app = application 
=======
app= application
>>>>>>> 288146822b593c279c952566e3b026657f274847
