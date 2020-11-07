def  directions():
  direction = ["Move Forward", "Move Backward", "Turn Left" and "Turn Right"]
  return direction

def menu():
  print("Please select a direction.")
  dirs = directions()
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")

def run():
  menu()

run()