#!/bin/bash

savename=$1
exec factorio/bin/x64/factorio \
    --start-server "./saves/$savename" \
    --server-settings ./saves/server-settings.json \
    --use-server-whitelist \
    --server-whitelist ./saves/server-whitelist.json \
    --server-banlist ./saves/server-banlist.json \
    --server-adminlist ./saves/server-adminlist.json
