import logging
from django.conf import settings
from pytz import timezone


TZ = timezone(settings.TIME_ZONE)

logger = logging.getLogger('log')
