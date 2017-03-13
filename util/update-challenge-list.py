#!/usr/bin/env python
#
# This script will fetch a list of challenges from hackerrank.com
# and save it to '/challenges.json'
#
# Dependency:
# * scrapy >=1.3
#
# This script is compatible with python 2.7 and 3.x (if applicable)

import functools
import json
import os.path
import scrapy
import scrapy.crawler

tracks = []

class HackerSpider(scrapy.Spider):
  name = 'list-challenge'
  
  def start_requests(self):
    tracks_list = [
      { 'title': 'Algorithms', 'name': 'algorithms' },
      { 'title': 'Data Structures', 'name': 'data-structures' },
      { 'title': 'Mathematics', 'name': 'mathematics' },
      ]
    for i, track in enumerate(tracks_list):
      tracks.append({
        'title': track['title'],
        'name': track['name'],
        'chapters': [],
        })
      url = 'https://www.hackerrank.com/rest/contests/master/tracks/' + track['name'] + '/chapters'
      yield scrapy.Request(url=url, callback=functools.partial(self.parse_chapters, d={
        'track-id': i,
        }))
  
  def parse_chapters(self, response, d):
    json_object = json.loads(response.text)
    for i, chapter in enumerate(json_object['models']):
      tracks[d['track-id']]['chapters'].append({
        'title': chapter['name'],
        'name': chapter['slug'],
        'challenges': [None] * chapter['challenges_count'],
        })
      for offset in range(0, chapter['challenges_count'], 10):
        url = 'https://www.hackerrank.com/rest/contests/master/categories/' \
              + tracks[d['track-id']]['name'] + '%7C' + chapter['slug'] \
              + '/challenges?offset=' + str(offset) + '&limit=10'
        yield scrapy.Request(url=url, callback=functools.partial(self.parse_page, d={
          'track-id': d['track-id'],
          'chapter-id': i,
          'offset': offset,
          }))
      
  def parse_page(self, response, d):
    json_object = json.loads(response.text)
    for i, challenge in enumerate(json_object['models']):
      tracks[d['track-id']]['chapters'][d['chapter-id']]['challenges'][d['offset'] + i] = {
        'title': challenge['name'],
        'name': challenge['slug'],
        }
        
if __name__ == '__main__':
  
  process = scrapy.crawler.CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
    })
  process.crawl(HackerSpider)
  process.start()
  #challenges.sort(key=lambda x: x['id'])
  #challenges.sort(key=lambda x: x['chapter-id'])
  #challenges.sort(key=lambda x: x['track-id'])
  with open(os.path.realpath(os.path.dirname(__file__) + '/../challenges.json'), 'w') as f:
    result = {
      'tracks': tracks
      }
    f.write(json.dumps(result, indent=2, separators=(',', ': ')))
