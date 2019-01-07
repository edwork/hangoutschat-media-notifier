#!/bin/bash

#########
#!/bin/bash

grabbed_message="Grabbed: $radarr_movie_title - [$radarr_moviefile_quality]"

/usr/bin/python /home/radarr/chat.py "$grabbed_message"
