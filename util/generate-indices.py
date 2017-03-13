#!/usr/bin/python3

import json
import os.path

def anchor_from_title(title):
  return '-'.join(title.lower().split())

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
        path_to_challenge = 'solution/practice/%s/%s/%s' % (track['name'], chapter['name'], challenge['name'])
        challenge['table-row'] = [str(i + 1), 
                                  '[%s](https://www.hackerrank.com/challenges/%s)' % (challenge['title'], challenge['name']),
                                  ]
        track['count'] += 1
        chapter['count'] += 1
        if os.path.exists(os.path.dirname(__file__) + '/../' + path_to_challenge):
          track['finish-count'] += 1
          chapter['finish-count'] += 1
          challenge['table-row'].append('[Solution & Comment](%s/solution.py)' % path_to_challenge)
        else:
          challenge['table-row'].append('WIP')
        
  # write to README.md
  fout.write('HackerRank Solutions in Python3\n======\n\n')
  for track in json_root['tracks']:
    fout.write('* [%s](#%s) (%d/%d)\n' % (track['title'], anchor_from_title(track['title']), track['finish-count'], track['count']))
  fout.write('\n')
  for track in json_root['tracks']:
    fout.write(track['title'] + '\n------\n\n')
    for chapter in track['chapters']:
      fout.write('* [%s](#%s) (%d/%d)\n' % (chapter['title'], anchor_from_title(chapter['title']), chapter['finish-count'], chapter['count']))
    fout.write('\n')
    for chapter in track['chapters']:
      fout.write('### %s\n' % chapter['title'])
      fout.write(' | '.join(['\\#', 'Challenge', 'Solution']) + '\n')
      fout.write('|'.join([':---:'] * 3) + '\n')
      for challenge in chapter['challenges']:
        fout.write(' | '.join(challenge['table-row']) + '\n')
      fout.write('\n')
  
