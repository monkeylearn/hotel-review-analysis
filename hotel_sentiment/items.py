# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelSentimentItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    stars = scrapy.Field()

class BookingReviewItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    positive_content = scrapy.Field()
    negative_content = scrapy.Field()
    tags = scrapy.Field()
