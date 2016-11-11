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

class TripAdvisorReviewItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    review_stars = scrapy.Field()

    reviewer_id = scrapy.Field()
    reviewer_name = scrapy.Field()
    reviewer_level = scrapy.Field()
    reviewer_location = scrapy.Field()

    city = scrapy.Field()

    hotel_name = scrapy.Field()
    hotel_url = scrapy.Field()
    hotel_classs = scrapy.Field()
    hotel_address = scrapy.Field()
    hotel_locality = scrapy.Field()
    hotel_review_stars = scrapy.Field()
    hotel_review_qty = scrapy.Field()


class BookingReviewItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    positive_content = scrapy.Field()
    negative_content = scrapy.Field()
    tags = scrapy.Field()
