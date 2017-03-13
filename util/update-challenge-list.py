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

class HackerSpider(scrapy.Spider):
  name = 'list-challenge'
  
  def start_requests(self):
    tracks = [
      { 'title': 'Algorithms', 'name': 'algorithms' },
      { 'title': 'Data Structures', 'name': 'data-structures' },
      { 'title': 'Mathematics', 'name': 'mathematics' },
      ]
    for i, track in enumerate(tracks):
      d = {
        'track-id': i,
        'track-title': track['title'],
        'track-name': track['name'],
        }
      url = 'https://www.hackerrank.com/rest/contests/master/tracks/' + track['name'] + '/chapters'
      yield scrapy.Request(url=url, callback=functools.partial(self.parse_chapters, d=d))
  
  def parse_chapters(self, response, d):
    json_object = json.loads(response.text)
    for i, chapter in enumerate(json_object['models']):
      next_d = d.copy()
      next_d['chapter-id'] = i
      next_d['chapter-title'] = chapter['name']
      next_d['chapter-name'] = chapter['slug']
      next_d['count'] = chapter['challenges_count']
      next_d['current'] = 0
      url = 'https://www.hackerrank.com/rest/contests/master/categories/' + d['track-name'] + '%7C' + chapter['slug'] + '/challenges?offset=0&limit=10'
      yield scrapy.Request(url=url, callback=functools.partial(self.parse_page, d=next_d))
      
  def parse_page(self, response, d):
    json_object = json.loads(response.text)
    currentPageStart = d['current']
    for i, challenge in enumerate(json_object['models']):
      out = {
        'domain': 'practice',
        'track-id': d['track-id'],
        'track-title': d['track-title'],
        'track-name': d['track-name'],
        'chapter-id': d['chapter-id'],
        'chapter-title': d['chapter-title'],
        'chapter-name': d['chapter-name'],
        'id': currentPageStart + i,
        'title': challenge['name'],
        'name': challenge['slug'],
        }
      result.append(out)
    if d['current'] + 10 < d['count']:
      next_d = d.copy()
      next_d['current'] += 10
      url = 'https://www.hackerrank.com/rest/contests/master/categories/algorithms%7C' + d['chapter-name'] + '/challenges?offset=' + str(next_d['current']) + '&limit=10'
      yield scrapy.Request(url=url, callback=functools.partial(self.parse_page, d=next_d))
        
if __name__ == '__main__':
  result = []
  process = scrapy.crawler.CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
    })
  process.crawl(HackerSpider)
  process.start()
  result.sort(key=lambda x: x['id'])
  result.sort(key=lambda x: x['chapter-id'])
  result.sort(key=lambda x: x['track-id'])
  with open(os.path.realpath(os.path.dirname(__file__) + '/../challenges.json'), 'w') as f:
    f.write(json.dumps(result, indent=4, separators=(',', ': ')))
