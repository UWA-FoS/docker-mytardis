if os.getenv('MYTARDIS_NIFCERT_ENABLE', 'False') == 'True':
    INSTALLED_APPS += ( 'nifcert', )
    POST_SAVE_FILTERS.append(
        (
            "nifcert.filters.metadata_filter.make_filter",
            [],
        ),
    )
