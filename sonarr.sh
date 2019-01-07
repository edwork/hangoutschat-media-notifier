#!/bin/bash

grabbed_message="\
Grabbed: $sonarr_series_title - \
$sonarr_release_seasonnumber x $sonarr_release_episodenumbers - \
$sonarr_release_episodetitles [$sonarr_release_quality]"

/usr/bin/python /home/sonarr/chat.py "$grabbed_message"
