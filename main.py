# create list
def fruits():
  fruits = ["orange", "pear", "banana"]

  # add fruits to list
  fruits.append("grapes")
  fruits[1] = "grapefruit"
  fruits[2] = "kiwi"
  
  # return function
  return fruits

# run the list
def run():
  print(fruits())



# access a text file
# import the file type
import csv

#open the file (make sure it exists)
with open ("locations.csv") as csvfile:
  # read only file, should be seperated using commas and speach marks
  csv_reader=csv.reader(csvfile,delimiter=',',quotechar='"')
  # for all rows in the read only file it must print the first word from the list
  for row in csv_reader:
    print(row[0])