# Bioformats
# https://github.com/keithschulze/mytardisbf
if os.getenv('MYTARDIS_BIOFORMATS_FILTER_ENABLE', 'False') == 'True':
    INSTALLED_APPS += ('mytardisbf',)
    MIDDLEWARE_CLASSES += ('tardis.tardis_portal.filters.FilterInitMiddleware',)
    FILTER_MIDDLEWARE = (("tardis.tardis_portal.filters", "FilterInitMiddleware"),)
    POST_SAVE_FILTERS = [
        ("mytardisbf.filters.metadata_filter.make_filter",
        ["BioformatsMetadata", "http://tardis.edu.au/schemas/bioformats/2",],),
    ]
