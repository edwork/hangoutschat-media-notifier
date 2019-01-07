#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Hangouts Chat - Webhook Argument Sender
###
Takes the first argument on the script and 
fires it to your Webhook 'bot' in Hangouts Chat
###
Configure by replacing the webhook below
###
"""

from httplib2 import Http
from json import dumps
import sys

"""Configure Here"""
webhook_url = "https://chat.googleapis.com/v1/spaces/XXXXXXXXXXXXXXXX"

message = sys.argv[1]

def main():
    url = selected_url
    bot_message = {
        'text' : message}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

if __name__ == '__main__':
    main()
