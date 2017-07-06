from settings_docker import *

INSTALLED_APPS += (
    'django_jasmine',
)

JASMINE_TEST_DIRECTORY = os.path.join(BASE_DIR,'tardis','tardis_portal','tests','jasmine')

