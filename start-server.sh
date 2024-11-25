#!/bin/bash

savename=$1
exec factorio/bin/x64/factorio --start-server "./saves/$savename" --server-settings ./saves/server-settings.json
