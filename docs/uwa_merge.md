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


