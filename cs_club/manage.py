#!/usr/bin/env python
import os
import sys
from setup import *
import time

apps="cs_app"
url_folder="cs_club"


if __name__ == '__main__':
    start_whoosh()
    create_view(apps)
    create_urls(url_folder,apps)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs_club.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
