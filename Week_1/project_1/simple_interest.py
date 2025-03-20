print("Welcome to the simple interest calculator")
principle = float(input("How much money did you invest?\n"))
rate = float(input("At what rate is the bank paying your interest?\n"))
time = float(input("How long is the time period of investment ?(in years)\n"))

total_amount = str((principle + (principle * rate/100.0 * time)))
print("Your total amount is" + " " + total_amount)



