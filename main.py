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



run()