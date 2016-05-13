from nltk.tokenize import sent_tokenize
import unicodecsv as csv

#Given a string, returns a list with the opinion units it extracted
#from the string
def tokenize_into_opinion_units(text):
    output = []
    for str in sent_tokenize(text):
        for output_str in str.split(' but '):
            output.append(output_str)
    return output

#Take positive.csv and negative.csv and mix them into
#positiveandnegative.csv
#This has each unit tagged with its booking.com sentiment
#This is the data I tagged with Mechanical Turk
def positive_and_negative_to_full():
    fpos = open('positive.csv')
    positive_units = [row for row in csv.reader(fpos)]
    fneg = open('negative.csv')
    negative_units = [row for row in csv.reader(fneg)]
    for item in positive_units:
        item.append('positive')
    for item in negative_units:
        item.append('negative')
    del negative_units[0]
    positive_units[0][0] = 'review_content'
    positive_units[0][1] = 'sentiment'
    full = positive_units
    full.extend(negative_units)
    with open('positiveandnegative.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(full)



#this will open the review scraped data and write two files from that info:
#positive.csv, containing positive opinion units
#negative.csv, containing negative opinion units
if __name__ == "__main__":
    #There are some problems with unicode
    #TODO take the file name as argument

    #positive content:
    f = open('itemsBooking.csv')
    #divide the data into opinion units:
    positive = [tokenize_into_opinion_units(row[1]) for row in csv.reader(f)]
    positive_units = []
    for row in positive:
        for elem in row:
            newrow = elem.split(' but ')
            for newelem in newrow:
                positive_units.append(newelem)
    #transform the elements into lists so I can use writerows
    positive_units = [[row] for row in positive_units]
    with open('positive.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(positive_units)

    #negative content:
    f.seek(0)
    negative = [tokenize_into_opinion_units(row[4]) for row in csv.reader(f)]
    negative_units = []
    for row in negative:
        for elem in row:
            newrow = elem.split(' but ')
            for newelem in newrow:
                negative_units.append(newelem)
    negative_units = [[row] for row in negative_units]
    with open('negative.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(negative_units)
