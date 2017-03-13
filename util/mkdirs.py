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
  challenges = json.loads(f.read())
  print(len(challenges))
  for challenge in challenges:
    path_to_challenge = '/../solution/' + challenge['domain'] + '/'
    if challenge['domain'] == 'practice':
      path_to_challenge += challenge['track-name'] + '/' + challenge['chapter-name'] + '/' + challenge['name']
      try:
        os.makedirs(os.path.dirname(__file__) + path_to_challenge)
      except FileExistsError:
        pass
