import csv
with open("Practice_work/random.csv") as csvfile:
 csv_reader=csv.reader( csvfile,delimiter=',',quotechar='"')
 for row in csv_reader:
    print(row[5])