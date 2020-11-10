with open("Practice_work/random.txt") as file:
  data=file.read()
  print(data[1]) 
  print(data[5])
  print(data[6])


with open("Practice_work/random.txt") as file:
  for line in file:
    print(line)