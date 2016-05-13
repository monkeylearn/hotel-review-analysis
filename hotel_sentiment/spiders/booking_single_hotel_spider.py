import scrapy
from scrapy.loader import ItemLoader
from hotel_sentiment.items import BookingReviewItem


class BookingSpider(scrapy.Spider):
    name = "booking_singlehotel"
    start_urls = [
        #http://www.booking.com/hotel/us/new-york-inn.html,
        #add your url here
    ]

    #get its reviews page
    def parse(self, response):
        reviewsurl = response.xpath('//a[@class="show_all_reviews_btn"]/@href')
        url = response.urljoin(reviewsurl[0].extract())
        self.pageNumber = 1
        return scrapy.Request(url, callback=self.parse_reviews)

    #and parse the reviews
    def parse_reviews(self, response):
        for rev in response.xpath('//li[starts-with(@class,"review_item")]'):
            item = BookingReviewItem()
            #sometimes the title is empty because of some reason, not sure when it happens but this works
            title = rev.xpath('.//a[@class="review_item_header_content"]/span[@itemprop="name"]/text()')
            if title:
                item['title'] = title[0].extract()
                positive_content = rev.xpath('.//p[@class="review_pos"]//span/text()')
                if positive_content:
                    item['positive_content'] = positive_content[0].extract()
                negative_content = rev.xpath('.//p[@class="review_neg"]//span/text()')
                if negative_content:
                    item['negative_content'] = negative_content[0].extract()
                item['score'] = rev.xpath('.//span[@itemprop="reviewRating"]/meta[@itemprop="ratingValue"]/@content')[0].extract()
                #tags are separated by ;
                item['tags'] = ";".join(rev.xpath('.//li[@class="review_info_tag"]/text()').extract())
                yield item

        next_page = response.xpath('//a[@id="review_next_page_link"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_reviews)
