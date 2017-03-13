#!/usr/bin/python3
#
# This script will create a directory for each challenge
# listed in challenges.json. The path will consists of 
# properties of the challenge, such as domain, track, chapter
# and name.
#
# To get an up-to-date version of challenges.json, run
# 'update-challenge-list.py'.

import os
import os.path
import json

with open(os.path.dirname(__file__) + '/../challenges.json', 'r') as f:
  json_root = json.loads(f.read())
  for track in json_root['tracks']:
    for chapter in track['chapters']:
      for challenge in chapter['challenges']:
        path_to_challenge = '/../solution/practice/' + track['name'] + '/' + chapter['name'] + '/' + challenge['name']
        try:
          os.makedirs(os.path.dirname(__file__) + path_to_challenge)
        except FileExistsError:
          pass
