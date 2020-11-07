def search(file_name):
  print("searching...")

  with open(file_name) as file:
    for line in file:
      print(f"looked in {line[:-1]}.")

  print("...done!")

def run():
  search("data/files/txt/locations.txt")


run()