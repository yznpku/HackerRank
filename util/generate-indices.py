#!/usr/bin/python3

import json
import os.path

with open(os.path.dirname(__file__) + '/../challenges.json', 'r') as file_challenges, open(os.path.dirname(__file__) + '/../README.md', 'w') as fout:
  json_root = json.loads(file_challenges.read())
  
  # count finished challenges and prepare rows
  for track in json_root['tracks']:
    track['finish-count'] = 0
    track['count'] = 0
    for chapter in track['chapters']:
      chapter['finish-count'] = 0
      chapter['count'] = 0
      for i, challenge in enumerate(chapter['challenges']):
        path_to_challenge = 'solution/practice/' + track['name'] + '/' + chapter['name'] + '/' + challenge['name']    
        challenge['table-row'] = [i + 1, 
                                  '[' + challenge['title'] + '](https://www.hackerrank.com/challenges/' + challenge['name'] + ')',
                                  ]
        track['count'] += 1
        chapter['count'] += 1
        if os.path.exists(os.path.dirname(__file__) + '/../' + path_to_challenge):
          track['finish-count'] += 1
          chapter['finish-count'] += 1
          challenge['table-row'].append('[Solution & Comment](blob/' + path_to_challenge + '/solution.py)')
        
  # write to README.md
  fout.write('HackerRank Solutions in Python3\n======\n\n')
  for track in json_root['tracks']:
    fout.write(track['title'] \
               + '(' + str(track['finish-count']) \
               + '/' + str(track['count']) \
               + ')' + '\n------\n')

  
