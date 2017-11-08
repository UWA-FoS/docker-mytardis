from os import environ

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tardis.tardis_portal.auth.authorisation.ACLAwareBackend',
)

AUTH_PROVIDERS = (
    ('localdb', 'Local DB', 'tardis.tardis_portal.auth.localdb_auth.DjangoAuthBackend'),
)
if 'MYTARDIS_LDAP_URL' in environ:
    AUTH_PROVIDERS += (
        ('ldap', 'LDAP Auth', 'tardis.tardis_portal.auth.ldap_auth.ldap_auth'),
    )

AUTH_PROFILE_MODULE = 'tardis_portal.UserProfile'

DEFAULT_AUTH = 'localdb'

GROUP_PROVIDERS = (
    'tardis.tardis_portal.auth.localdb_auth.DjangoGroupProvider',
    'tardis.tardis_portal.auth.token_auth.TokenGroupProvider'
)

NEW_USER_INITIAL_GROUPS = []
