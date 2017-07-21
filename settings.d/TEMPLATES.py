# https://docs.djangoproject.com/en/1.8/ref/templates/

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'tardis','tardis_portal','templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'tardis.tardis_portal.context_processors'
                '.global_contexts',
                'tardis.tardis_portal.context_processors'
                '.single_search_processor',
                'tardis.tardis_portal.context_processors'
                '.tokenuser_processor',
                'tardis.tardis_portal.context_processors'
                '.registration_processor',
                'tardis.tardis_portal.context_processors'
                '.user_details_processor',
                'tardis.tardis_portal.context_processors'
                '.manage_account_processor',
                'tardis.tardis_portal.context_processors'
                '.google_analytics',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ],
        },
    }
]
