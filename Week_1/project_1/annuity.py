print("Welcome to the annuity plan calculator")
principle = float(input("How much money did you invest?\n"))
rate = float(input("At what rate is the bank paying your interest (in decimal)?\n"))
time = float(input("How long is the time period of investment ?(in years)\n"))
number_of_payment = float(input("How many times a year do you make payment ?\n"))
exponent = number_of_payment * time

future_value= str((principle * (((1.0 + rate/number_of_payment) ** (exponent - 1.0 )) / (rate / number_of_payment))))
print("Your future value is" + " " + future_value)
#FV = P * [((1 + r/n)^(nt) - 1) / (r/n)]

