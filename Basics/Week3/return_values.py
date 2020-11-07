def sums_weight(weight_bop,weight_beep):
  total_weight = weight_bop + weight_bop
  return total_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

def run():
  print("what is the weight of bop? ")
  bop_weight = float(input())

  print("what is the weight of beep? ")
  beep_weight = float(input())

  print("What would you like to calculate(sum or average)?")
  action = input() 

  if (action == "sum"):
    answer = sums_weight(beep_weight, bop_weight)
    print("the sum of beep's and bop's weight is {:.2f}".format(answer))
  elif (action == "average"):
    answer = calc_avg_weight(beep_weight, bop_weight)
    print("The average of Beep's and bop's weight is {:.2d}".format(answer))
  else:
    print("I am not sure what you would like to do")

run()