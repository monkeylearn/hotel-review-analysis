import unicodecsv as csv
import json
import re

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#local instance of elasticsearch, you can change this
es = Elasticsearch(['http://localhost:9200'])

#index the reviews
filename = "keys_tripadvisor_bangkok.csv"
f = open(filename)
reference = ["city",                #0
             "hotel_locality",      #1
             "reviewer_location",   #2
             "hotel_url",           #3
             "title",               #4
             "content",             #5
             "hotel_address",       #6
             "hotel_class",         #7
             "hotel_review_stars",  #8
             "hotel_review_qty",    #9
             "review_stars",        #10
             "hotel_name",          #11
             "key"                  #12
            ]

chunk_count = 0
actions = []
csv.reader(f).next()
for row in csv.reader(f):

    item = {}
    for i in range(12):
        item[reference[i]] = row[i]

    if item["hotel_review_qty"] != "":
        item["hotel_review_qty"] = re.sub(",", "", item["hotel_review_qty"].split(" ")[0])

    if item["hotel_class"] != "":
        item["hotel_class"] = item["hotel_class"].split(" ")[0]

    if item["hotel_review_stars"] != "":
        item["hotel_review_stars"] = item["hotel_review_stars"].split(" ")[0]

    if item["review_stars"] != "":
        item["review_stars"] = item["review_stars"].split(" ")[0]

    action = {
            "_index": "index_hotels_3",
            "_type": "review",
            "_id": row[12],
            "_source": item
            }
    actions.append(action)
    chunk_count += 1
    #use chunks of 10000 items
    if chunk_count == 10000:
        helpers.bulk(es, actions)
        chunk_count = 0
        actions = []

if chunk_count > 0:
    helpers.bulk(es, actions)
    print "leftovers"

#index the classified opinion units
