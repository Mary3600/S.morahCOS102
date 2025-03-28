import cmath

print("Welome to the equation calculator ")
print("1. Quadratic equation \n2. Cubic equation \n3. Quartic equation")
option = input("What would you like to calculate today? (1, 2 or 3): ")
if option == '1':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = (b**2) - (4*a*c)
    x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    print("The roots of your equation are: ", x1, x2)
    
elif option == '2':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))

elif option == '3':
    a = float(input("Enter a:"))
    