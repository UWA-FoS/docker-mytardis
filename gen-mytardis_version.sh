#!/usr/bin/env bash

export GIT_EXEC_PATH='src/mytardis/'

commit_id="$(git log -1 --format='%H')"
date="$(git log -1 --format='%cd' --date=rfc)"
branch="$(git rev-parse --abbrev-ref HEAD)"
tag="$(git describe --abbrev=0 --tags 2>/dev/null)"

echo "MYTARDIS_MYTARDIS_VERSION={'commit_id': '${commit_id}', 'date': '${date}', 'tag': '${tag}', 'branch': '${branch}'}"
