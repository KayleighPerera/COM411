import os

def cwd():
  path = os.getcwd()
  print(f"The current wworking folder is {path}")

  print("The folder contains the following:")
  for file in os.listdir(path):
    path(file)

def run():
  print("processing...")
  cwd()
 
run()