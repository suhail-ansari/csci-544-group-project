# -*- coding: utf-8 -*-
import scrapy


class ESPNUSCommentarySpider(scrapy.Spider):
  name = 'espn_us_commentary'

  def __init__(self, start_id=458800, limit=10):
    self.start_urls = ['http://www.espnfc.us/commentary?gameId=' + str(start_id)]
    self.limit = int(limit)

  def parse(self, response):
    for tr in response.css('div[data-behavior=soccer_commentary] tr'):
      yield {
        'time': tr.css('td.time-stamp::text').extract_first(),
        'text': tr.css('td.game-details::text').extract_first().strip()
      }

    if self.limit > 0:
      self.limit -= 1
      _, game_id  = response.url.rsplit('=', 1)
      next_page = 'http://www.espnfc.us/commentary?gameId=' + str(int(game_id) + 1)
      yield scrapy.Request(next_page, callback=self.parse)
