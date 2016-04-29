import scrapy
from scrapy.loader import ItemLoader
from hotel_sentiment.items import BookingReviewItem

max_pages_per_hotel = 6

class BookingSpider(scrapy.Spider):
    name = "booking"
    start_urls = [
        "http://www.booking.com/searchresults.html?aid=357026&label=gog235jc-city-XX-us-newNyork-unspec-uy-com-L%3Axu-O%3AosSx-B%3Achrome-N%3Ayes-S%3Abo-U%3Ac&sid=b9f9f1f142a364f6c36f275cfe47ee55&dcid=4&city=20088325&class_interval=1&dtdisc=0&from_popular_filter=1&hlrd=0&hyb_red=0&inac=0&label_click=undef&nflt=di%3D929%3Bdistrict%3D929%3B&nha_red=0&postcard=0&redirected_from_city=0&redirected_from_landmark=0&redirected_from_region=0&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&ss_all=0&ssb=empty&sshis=0&rows=15&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID;sid=b9f9f1f142a364f6c36f275cfe47ee55;dcid=12;checkin=2016-05-19;checkout=2016-05-20;city=20021296&;ilp=1;lp_index_textlink2srdaterec=1&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID;sid=b9f9f1f142a364f6c36f275cfe47ee55;dcid=12;checkin=2016-05-18;checkout=2016-05-19;city=20023182&;ilp=1;lp_index_textlink2srdaterec=1&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fus%2Fboston.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%3Bthm%3Dhotel%26%3B&city=20061717&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fus%2Flas-vegas.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Bilp%3D1%3Binac%3D0%3Bpoff%3D0%26%3B&city=20079110&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Ffr%2Fparis.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Bilp%3D1%3Binac%3D0%3Bpoff%3D0%26%3B&city=-1456928&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fes%2Fmadrid.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Bilp%3D1%3Binac%3D0%3Bpoff%3D0%26%3B&city=-390625&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Far%2Fbuenos-aires.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Bilp%3D1%3Binac%3D0%3Bpoff%3D0%26%3B&city=-979186&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fus%2Flos-angeles.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=20014181&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fbr%2Frio-de-janeiro.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-666610&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fbr%2Fsao-paulo.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-671824&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fgb%2Flondon.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-2601889&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fgb%2Fliverpool.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-2601422&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fgb%2Fedinburgh.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-2595386&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fes%2Fbarcelona.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-372490&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fit%2Frome.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-126693&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1",
        "http://www.booking.com/searchresults.html?dcid=12&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID&sid=b9f9f1f142a364f6c36f275cfe47ee55&src=city&si=ai%2Cco%2Cci%2Cre%2Cdi&error_url=http%3A%2F%2Fwww.booking.com%2Fcity%2Fit%2Fvenice.html%3Flabel%3Dgen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaO0BiAEBmAExuAEPyAEP2AED6AEB-AEDqAID%3Bsid%3Db9f9f1f142a364f6c36f275cfe47ee55%3Bdcid%3D12%3Binac%3D0%3Bpoff%3D0%26%3B&city=-132007&checkin_monthday=18&checkin_year_month=2016-5&checkout_monthday=19&checkout_year_month=2016-5&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&tfl_cwh=1"        
    ]

    pageNumber = 1

    #for every hotel
    def parse(self, response):
        for hotelurl in response.xpath('//a[@class="hotel_name_link url"]/@href'):
            url = response.urljoin(hotelurl.extract())
            yield scrapy.Request(url, callback=self.parse_hotel)

        next_page = response.xpath('//a[starts-with(@class,"paging-next")]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    #get its reviews page
    def parse_hotel(self, response):
        reviewsurl = response.xpath('//a[@class="show_all_reviews_btn"]/@href')
        url = response.urljoin(reviewsurl[0].extract())
        self.pageNumber = 1
        return scrapy.Request(url, callback=self.parse_reviews)

    #and parse the reviews
    def parse_reviews(self, response):
        if self.pageNumber > max_pages_per_hotel:
            return
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
            self.pageNumber += 1
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_reviews)
