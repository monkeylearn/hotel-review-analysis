import sys
import unicodecsv as csv
import json

from elasticsearch import Elasticsearch
from elasticsearch import helpers

#filename = "classified_opinion_units_keys_tripadvisor_bangkok.csv"
#takes two arguments:
#   the name of the file to index
#   the starting index for the id
#       the ids shouldn't overlap or you will replace existing opinion units
#IMPORTANT: before indexing opinion units you must index the parent reviews
filename =  sys.argv[1]
cont_id = int(sys.argv[2])
f = open(filename)
reference = ["review_key",
             "content",
             "sentiment",
             "sent_probability",
             "topic"
            ]

es = Elasticsearch(['http://localhost:9200'])
#index by chunk of 10000 items
chunk_count = 0
actions = []

for row in csv.reader(f):
    item = {}

    for i in range(len(reference)):
        item[reference[i]] = row[i]
    action = {
            "_index": "index_hotels_3",
            "_type": "opinion_unit",
            "_id": cont_id,
            "_parent": row[0],
            "_source": item
            }
    actions.append(action)

    chunk_count += 1

    if chunk_count == 10000:
        helpers.bulk(es, actions)
        chunk_count = 0
        actions = []
        print "indexed %d" %cont_id

    cont_id += 1

if chunk_count > 0:
    helpers.bulk(es, actions)
    print "leftovers"
    print "indexed %d" %cont_id
