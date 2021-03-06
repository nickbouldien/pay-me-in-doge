"""
WSGI config for pay_me_in_doge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pay_me_in_doge.settings")

application = get_wsgi_application()

# if __name__ == "__main__":
#     application.run(host="0.0.0.0")
