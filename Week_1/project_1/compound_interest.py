print("Welcome to the compound interest calculator")
principle = float(input("How much money did you invest?\n"))
rate = float(input("At what rate is the bank paying your interest (in decimal)?\n"))
time = float(input("How long is the time period of investment ?(in years)\n"))
number_of_compounding = float(input("How often is the money componded per year\n"))
exponent = number_of_compounding * time

total_amount = str((principle * (1.0 + rate/number_of_compounding) ** exponent ))
print("Your total amount is" + " " + total_amount)

