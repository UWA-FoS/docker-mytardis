from datetime import timedelta

def get_admin_media_path():
    import pkgutil
    package = pkgutil.get_loader("django.contrib.admin")
    return os.path.join(package.filename, 'static', 'admin')

ACCOUNT_ACTIVATION_DAYS = 3

ADMIN_MEDIA_STATIC_DOC_ROOT = get_admin_media_path()

ARCHIVE_FILE_MAPPERS = {'deep-storage': ('tardis.apps.deep_storage_download_mapper.mapper.deep_storage_mapper',)}
AUTOGENERATE_API_KEY = False
BLEACH_ALLOWED_ATTRIBUTES = {'a': ['href', 'title'], 'acronym': ['title'], 'abbr': ['title']}
BLEACH_ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul']

DATASET_VIEWS = []
DEFAULT_ARCHIVE_FORMATS = ['tar']
DEFAULT_ARCHIVE_ORGANIZATION = 'deep-storage'
DEFAULT_FILE_STORAGE = 'tardis.tardis_portal.storage.MyTardisLocalFileSystemStorage'
DEFAULT_MIGRATION_DESTINATION = 'unknown'
DOI_APP_ID = ''
DOI_BASE_URL = 'http://mytardis.example.com'
DOI_ENABLE = False
DOI_MINT_URL = 'https://services.ands.org.au/home/dois/doi_mint.php'
DOI_NAMESPACE = 'http://www.tardis.edu.au/schemas/doi/2011/12/07'
DOI_RELATED_INFO_ENABLE = False
DOI_TEMPLATE_DIR = 'tardis_portal/doi/'
DOI_XML_PROVIDER = 'tardis.tardis_portal.ands_doi.DOIXMLProvider'
DOWNLOAD_ARCHIVE_SIZE_LIMIT = 0
DOWNLOAD_SPACE_SAFETY_MARGIN = 8388608
DOWNLOAD_TEMP_DIR = '/tmp'
EXPERIMENT_VIEWS = []
INDEX_VIEWS = {}
INITIAL_LOCATIONS = {}
MANAGE_ACCOUNT_ENABLED = True
MAX_IMAGES_IN_CAROUSEL = 100
MODULE_LOG_FILENAME = 'tardis.log'
MODULE_LOG_LEVEL = 'INFO'
MODULE_LOG_MAXBYTES = 0
MYTARDIS_VERSION = {'commit_id': '', 'date': '', 'tag': '', 'branch': ''}
OAIPMH_PROVIDERS = ['tardis.apps.oaipmh.provider.experiment.DcExperimentProvider', 'tardis.apps.oaipmh.provider.experiment.RifCsExperimentProvider']
OAI_DOCS_PATH = os.path.join(BASE_DIR,'var','oai')
RAPID_CONNECT_CONFIG = {'iss': 'https://rapid.test.aaf.edu.au', 'authnrequest_url': '', 'secret': 'CHANGE_ME', 'aud': 'https://example.com/rc/'}
RAPID_CONNECT_ENABLED = False
REDIS_VERIFY_DELAY = 86400
REDIS_VERIFY_MANAGER = False
REDIS_VERIFY_MANAGER_SETUP = {'host': 'localhost', 'db': 1, 'port': 6379}
REGISTRATION_OPEN = True
RELATED_INFO_SCHEMA_NAMESPACE = 'http://www.tardis.edu.au/schemas/related_info/2011/11/10'
RELATED_OTHER_INFO_SCHEMA_NAMESPACE = 'http://www.tardis.edu.au/schemas/experiment/annotation/2011/07/07'
RENDER_IMAGE_SIZE_LIMIT = 0
REQUIRE_DATAFILE_CHECKSUMS = 'True'
REQUIRE_DATAFILE_SIZES = 'True'
REQUIRE_VALIDATION_ON_INGESTION = 'True'
REQUIRE_VALID_PUBLIC_CONTACTS = True
RIFCS_GROUP = 'MyTARDIS Default Group'
RIFCS_KEY = 'keydomain.example'
RIFCS_PROVIDERS = ('tardis.tardis_portal.publish.provider.rifcsprovider.RifCsProvider',)
RIFCS_TEMPLATE_DIR = '/srv/mytardis/tardis/tardis_portal/templates/tardis_portal/rif-cs/profiles/'
SFTP_GEVENT = False
SFTP_HOST_KEY = '-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKCAIEAl7sAF0x2O/HwLhG68b1uG8KHSOTqe3Cdlj5i/1RhO7E2BJ4B\n3jhKYDYtupRnMFbpu7fb21A24w3Y3W5gXzywBxR6dP2HgiSDVecoDg2uSYPjnlDk\nHrRuviSBG3XpJ/awn1DObxRIvJP4/sCqcMY8Ro/3qfmid5WmMpdCZ3EBeC0CAwEA\nAQKCAIBSGefUs5UOnr190C49/GiGMN6PPP78SFWdJKjgzEHI0P0PxofwPLlSEj7w\nRLkJWR4kazpWE7N/bNC6EK2pGueMN9Ag2GxdIRC5r1y8pdYbAkuFFwq9Tqa6j5B0\nGkkwEhrcFNBGx8UfzHESXe/uE16F+e8l6xBMcXLMJVo9Xjui6QJBAL9MsJEx93iO\nzwjoRpSNzWyZFhiHbcGJ0NahWzc3wASRU6L9M3JZ1VkabRuWwKNuEzEHNK8cLbRl\nTyH0mceWXcsCQQDLDEuWcOeoDteEpNhVJFkXJJfwZ4Rlxu42MDsQQ/paJCjt2ONU\nWBn/P6iYDTvxrt/8+CtLfYc+QQkrTnKn3cLnAkEAk3ixXR0h46Rj4j/9uSOfyyow\nqHQunlZ50hvNz8GAm4TU7v82m96449nFZtFObC69SLx/VsboTPsUh96idgRrBQJA\nQBfGeFt1VGAy+YTLYLzTfnGnoFQcv7+2i9ZXnn/Gs9N8M+/lekdBFYgzoKN0y4pG\n2+Q+Tlr2aNlAmrHtkT13+wJAJVgZATPI5X3UO0Wdf24f/w9+OY+QxKGl86tTQXzE\n4bwvYtUGufMIHiNeWP66i6fYCucXCMYtx6Xgu2hpdZZpFw==\n-----END RSA PRIVATE KEY-----\n'
SFTP_PORT = 2200
SFTP_USERNAME_ATTRIBUTE = 'email'
SINGLE_SEARCH_ENABLED = False
SITE_ID = 1
SPONSORED_TEXT = None
STAGING_MOUNT_PREFIX = 'smb://localhost/staging/'
STAGING_MOUNT_USER_SUFFIX_ENABLE = False

STAGING_PROTOCOL = 'ldap'
STATICFILES_DIRS = (('admin', ADMIN_MEDIA_STATIC_DOC_ROOT),)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATIC_DOC_ROOT = os.path.join(BASE_DIR,'tardis','tardis_portal','site_media')

SYSTEM_LOG_FILENAME = 'request.log'
SYSTEM_LOG_LEVEL = 'INFO'
SYSTEM_LOG_MAXBYTES = 0

TOKEN_EXPIRY_DAYS = 30
TOKEN_LENGTH = 30
TOKEN_USERNAME = 'tokenuser'
TRANSFER_PROVIDERS = {'local': 'tardis.tardis_portal.transfer.LocalTransfer', 'dav': 'tardis.tardis_portal.transfer.WebDAVTransfer', 'http': 'tardis.tardis_portal.transfer.SimpleHttpTransfer'}
UPLOADIFY_PATH = '%s/%s' % (STATIC_URL,'js/lib/uploadify')
UPLOADIFY_UPLOAD_PATH = '%s/%s' % (MEDIA_URL,'uploads')
UPLOAD_METHOD = False
USER_PROVIDERS = ('tardis.tardis_portal.auth.localdb_auth.DjangoUserProvider',)
