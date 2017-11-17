# http://docs.celeryproject.org/en/3.1/configuration.html
from datetime import timedelta

CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'rpc://')

CELERYBEAT_SCHEDULE = {'verify-files': {'task': 'tardis_portal.verify_dfos', 'schedule': timedelta(0, 300)}}

CACHES.update(
    { 'celery-locks': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'celery_lock_cache',
    }, }
)
