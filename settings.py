import djcelery

INSTALLED_APPS += (
    'django_celery',
    'django_jasmine',
)

# Celery and RabbitMQ
BROKER_URL = os.getenv('MYTARDIS_BROKER_URL', 'pyamqp://guest@rabbitmq//')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'rpc://')
CACHES += {
    'celery-locks': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'celery_lock_cache',
    },
}

JASMINE_TEST_DIRECTORY = os.path.join(BASE_DIR,'tardis','tardis_portal','tests','jasmine')

