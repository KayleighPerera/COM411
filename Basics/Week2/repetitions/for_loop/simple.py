# ask how many mountains to display
print ("how many mountains should i display?")
mountains = int(input())

# display mountains 
print("\nDisplaying...")

for mountain in range (mountains):
  print("""
  
           --
         /    \\_
       /^        \\
     /    ^       \\
   _/   ^ ^       ^\\_
  / ^        ^      \\

""")