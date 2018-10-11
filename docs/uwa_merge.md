# Merge TruDat specific code for deployment

```bash
cd ./src/mytardis
git remote add trudat https://github.com/UWA-FoS/trudat.git
git fetch trudat
git merge trudat/uwa-deploy
```

```bash
$ git remote -v
origin  https://github.com/mytardis/mytardis.git (fetch)
origin  https://github.com/mytardis/mytardis.git (push)
trudat  https://github.com/UWA-FoS/trudat.git (fetch)
trudat  https://github.com/UWA-FoS/trudat.git (push)

$ git merge trudat/uwa-deploy
Auto-merging tardis/urls.py
Auto-merging tardis/tardis_portal/views/utils.py
CONFLICT (content): Merge conflict in tardis/tardis_portal/views/utils.py
Auto-merging tardis/tardis_portal/views/pages.py
Auto-merging tardis/tardis_portal/views/authentication.py
Auto-merging tardis/tardis_portal/jstemplates/tardis_portal/dataset_tile.html
Automatic merge failed; fix conflicts and then commit the result.
```

```
            obj['facility'] = dataset.instrument.facility.name

<<<<<<< HEAD
    # Whether dataset thumbnails are enabled, i.e.
    # include a thumbnail <div> in every tile:
    obj['show_dataset_thumbnails'] = getattr(
        settings, "SHOW_DATASET_THUMBNAILS", True)

    # Whether this dataset tile's thumbnail is enabled.
    # If not, still include a blank thumbnail <div>:
=======
        # Customisation for UWA's TruDat + NIFCert MyTardis configuration.
        rda_handle = get_instrument_rda_handle(dataset.instrument.id)
        if rda_handle:
            obj['instrument_rda_handle'] = rda_handle

>>>>>>> trudat/uwa-deploy
    if include_thumbnail:
```


