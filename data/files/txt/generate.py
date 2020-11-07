def search(file_name):
  print("Searching...")
  sections = []
  books = []

  with open (file_name) as file:
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        sections.append(parts[1].replace('\n'''))
      else:
        books.append(line.replace('\n'))
  
  print("done")

  return(sections, books)
  