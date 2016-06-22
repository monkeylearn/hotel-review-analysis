# Sentiment Analysis and Aspect classification for Hotel Reviews

This is the source code of MonkeyLearn's series of posts related to analyzing sentiment and aspects from hotel reviews using machine learning models.

### Code organization

The project itself is a Scrapy project that is used to gather training and testing data from different sites like TripAdvisor and Booking. Besides a series of Python and Jupyter notebooks to implement some necessary scripts.

### [Creating a sentiment analysis model with Scrapy and MonkeyLearn](https://blog.monkeylearn.com/creating-sentiment-analysis-model-with-scrapy-and-monkeylearn/)

The TripAdvisor (hotel_sentiment/spider/tripadvisor_spider.py) spider is used to gather data to train a sentiment analysis classifier in MonkeyLearn. Reviews texts are used as the sample content and reviews stars are used as the category (1 and 2 stars = Negative, 4 and 5 stars = Positive).

To crawl ~15000 items from tripadvisor use:
```sh
scrapy crawl tripadvisor -o itemsTripadvisor.csv -s CLOSESPIDER_ITEMCOUNT=15000
```
You can check out the generated machine learning sentiment analysis model [here](https://app.monkeylearn.com/categorizer/projects/cl_rZ2P7hbs/tab/main-tab).

### [Getting actionable insights from reviews using Machine Learning - Part 1](https://blog.monkeylearn.com/getting-actionable-insights-from-reviews-using-machine-learning-part1/)

The Booking spider (hotel_sentiment/spider/booking_spider.py) is used to gather data to train an aspect classifier in MonkeyLearn. The data obtained with this spider can be manually tagged with each aspect (eg: cleanliness, comfort & facilities, food, internet, location, staff, value for money) using MonkeyLearn's Sample tab or an external crowd sourcing service like Mechanical Turk.

To crawl from booking use:
```sh
scrapy crawl booking -o itemsBooking.csv
```

You first have to add the url of a starting city. To crawl from a single hotel in booking use:

```sh
scrapy crawl booking_singlehotel -o <hotel name>.csv
```

- ```opinionTokenizer.py``` is a simple script to obtain the "opinion units" from each review.
- ```classify_and_plot_reviews.ipynb``` is a simple script that uses the generated model to classify new reviews and then plot the results in a graph using Plotly.

You can check out the generated machine learning aspect classifier [here](https://app.monkeylearn.com/categorizer/projects/cl_TKb7XmdG/tab/main-tab).
