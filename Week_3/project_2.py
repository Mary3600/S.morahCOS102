print("Welcome to the annual tax revenue calculator")

work_xp = int(input("How many years of work experience do you have? - "))
age = int(input("How old are you? - "))

if work_xp > 25 and age >= 55:
    print("Your annual tax revenue is ₦5,600,000")

elif work_xp > 20 and age>= 45:
    print("Your annual tax revenue is ₦4,480,000")

elif work_xp > 10 and age >= 35:
    print("Your annual tax revenue is ₦1,500,000")

else:
    print("Your annual tax revenue is ₦550,000")