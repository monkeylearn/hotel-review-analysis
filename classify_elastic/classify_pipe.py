import unicodecsv as csv
filename = "<the name of the csv with the opinion units>"
f = open(filename)

samples = []
count = 0
# if the script broke for some reason and you have already classified part of your data
# uncomment this code to skip the first to_skip items
# to_skip = 10000
# for row in csv.reader(f):
# 	count += 1
# 	if count == to_skip:
# 		break

from monkeylearn import MonkeyLearn
ml = MonkeyLearn("<your api key here>")
module_id = 'pi_YKStimMw'


csvfile = open("classified_" + filename, 'ab')
writer = csv.writer(csvfile,dialect='excel')

chunk_count = 0
chunk = []
for row in csv.reader(f):
	chunk.append(row)
	count+=1
	chunk_count+=1
	if chunk_count == 500:
		data = {
			"texts": [{"text": sample[1]} for sample in chunk]
		}
		res = ml.pipelines.run(module_id, data, sandbox=False)
		for i in range(len(chunk)):
			#single label classifier
			sentiment = res.result['tags'][i]['sentiment'][0]['label']
			chunk[i].append("/" + sentiment)
			#probability!
			probability = res.result['tags'][i]['sentiment'][0]['probability']
			chunk[i].append(probability)

			#multi label with only one level
			tags_topic_list = []
			for tags_topic in res.result['tags'][i]['topic']:
					tags_topic_list.append("/" + tags_topic[0]['label'])

			chunk[i].append(":".join(tags_topic_list))
			#not considering the probability because thats hard to save

		writer.writerows(chunk)
		chunk = []
		chunk_count = 0

		print "wrote %d" %count

csvfile.close()
f.close()
