import djcelery
from datetime import timedelta

INSTALLED_APPS += (
    'djcelery',
)

BROKER_URL = os.getenv('MYTARDIS_BROKER_URL', 'pyamqp://guest@rabbitmq/')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'rpc://')

CELERYBEAT_SCHEDULE = {'verify-files': {'task': 'tardis_portal.verify_dfos', 'schedule': timedelta(0, 300)}}

CACHES.update(
    { 'celery-locks': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'celery_lock_cache',
    }, }
)

