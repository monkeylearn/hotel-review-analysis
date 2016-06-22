import unicodecsv as csv
import hashlib
from opinionTokenizer import tokenize_into_opinion_units

filename = "tripadvisor_bangkok.csv"
f = open(filename)
samples = [row for row in csv.reader(f)]
samples[0].append("key")

for i in range(1,len(samples)):
    key =  hashlib.md5(samples[i][5].encode('utf-8')).hexdigest()
    samples[i].append(key)

#write the reviews with the keys, this file will be used for indexing
with open('keys_' + filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(samples)


opinion_units = []
for i in range(1,len(samples)):
    key = samples[i][12]
    for opinion_unit in tokenize_into_opinion_units(samples[i][4]) + tokenize_into_opinion_units(samples[i][5]):
        opinion_units.append([key, opinion_unit])

#write the opinion units with the key of the parent review
with open('opinion_units_keys_' + filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(opinion_units)
