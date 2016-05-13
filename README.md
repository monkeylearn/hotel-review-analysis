# hotel-reviews-sentiment
Scraping hotel reviews from TripAdvisor and Booking.com for sentiment and topic analysis.


To crawl ~15000 items from tripadvisor use "scrapy crawl tripadvisor -o itemsTripadvisor.csv -s CLOSESPIDER_ITEMCOUNT=15000"

To crawl from booking use "scrapy crawl booking -o itemsBooking.csv"
(first you have to add the url of a starting city)

To crawl from a single hotel in booking use "scrapy crawl booking_singlehotel -o <hotel name>.csv"
(first you have to add the url of a hotel)
