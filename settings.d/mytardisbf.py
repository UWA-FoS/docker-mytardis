# Bioformats
# https://github.com/keithschulze/mytardisbf
# Celery worker settings
# - run Bioformats filter outside of the default celery queue
#   BIOFORMATS_QUEUE = "nameofqueue"
# - The maximum heap space use by the JVM in each celery worker
#   MTBF_MAX_HEAP_SIZE = "1G"
if os.getenv('MYTARDIS_BIOFORMATS_ENABLE', 'False') == 'True':
    INSTALLED_APPS += ('mytardisbf',)
    MIDDLEWARE_CLASSES += ('tardis.tardis_portal.filters.FilterInitMiddleware',)
    FILTER_MIDDLEWARE += (("tardis.tardis_portal.filters", "FilterInitMiddleware"),)
    POST_SAVE_FILTERS.append(
        ("mytardisbf.filters.metadata_filter.make_filter",
        ["BioformatsMetadata", "http://tardis.edu.au/schemas/bioformats/2",],),
    )
