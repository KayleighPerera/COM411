def short_pattern():
  pattern = {"sequence":"101",
"occurrences":5}
return pattern

def medium_mattern():
  pattern ={"sequence":"11100",
  "occurrences":25
  }

return pattern

def long_pattern():
  pattern = {"sequence":"1100110011001100", "occurrences":50 }

return pattern

def run():
  print("analysing patterns")

  patterns = {"short sequence": short_pattern(),
  "medium sequence": medium_pattern(),
  "long sequence": long_pattern()
  }

 print(patterns)

run()