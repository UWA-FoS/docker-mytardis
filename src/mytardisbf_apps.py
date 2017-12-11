import logging
from django.apps import AppConfig
from tardis.tardis_portal.models import Schema

logger = logging.getLogger(__name__)


class MyTardisBFConfig(AppConfig):
    name = 'mytardisbf'
    verbose_name = "MyTardis Bioformats"

