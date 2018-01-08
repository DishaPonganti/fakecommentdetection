'''
Author Jai Prakash(prakashjai01@gmail.com)
Change Log
1. 8/jan/2018 Jai Added CreateCSVFile & checkNull Functions
'''
import csv

# this file will convert database in proper csv with required fields only
from app.helper.ConnectionDb import getDbConnection


def CreateCSVFile():
    data_db = getDbConnection()
    db_data = data_db['new_data_set'].find().limit(1000)

    with open('electronics.csv', 'wt') as csvfile:
        # if we use other options with file writer, we may loose commas in comments
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['ReviewText','SummaryText','ProductName','Helpful',  'Overall', 'unixtime','Fake_NonFake', 'Fake_Category','SentimentScore'])
        for singleRecord in db_data:
            listToBePushed = []
            listToBePushed.append(checkNull(singleRecord['reviewText']))
            listToBePushed.append(checkNull(singleRecord['summary']))
            listToBePushed.append('-')
            listToBePushed.append(checkNull(singleRecord['helpful']))
            listToBePushed.append(checkNull(singleRecord['overall']))
            listToBePushed.append(checkNull(singleRecord['unixReviewTime']))
            listToBePushed.append('1')
            listToBePushed.append('1')
            listToBePushed.append('0')
            # print(listToBePushed)
            filewriter.writerow(listToBePushed)
          

def checkNull (objectToBeChecked):
    if objectToBeChecked is None:
        return ''
    else:
        return objectToBeChecked

CreateCSVFile()