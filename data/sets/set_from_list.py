def observed():
  observations = []

  for count in range(7):
    print("please enter an item")
    item = input()
    observations.append(item)

  return observations

def run():
  print("counting observations...")
  observations = observed()
  
  observations_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
    observations_set.add( (observation, occurrences) )

  for key in observations_set:
    print(f"{key} observed {occurrences} times.")

run()