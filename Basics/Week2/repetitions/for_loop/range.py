# Ask what level of brightness is requires
print("what level of brightness is required?")
brightness = int(input())

# Adjusting the brightness
print("\nAdjusting brightness")

for brightness in range(2, brightness + 1, 2):
  print("Beep's brightness level:","*" * brightness)
  print("Bop's brightness level:", "*" * brightness)

print("Adjustments complete!")