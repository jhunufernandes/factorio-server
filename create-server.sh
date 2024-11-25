#!/bin/bash

savename=$1
exec factorio/bin/x64/factorio \
    --create "./saves/$savename" \
    --map-gen-settings ./saves/map-gen-settings.json \
    --map-settings ./saves/map-settings.json
