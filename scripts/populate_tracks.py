#!/usr/bin/env python
import requests

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

from main.models import Genres
