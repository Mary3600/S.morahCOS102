'''
radius = float(input("What is the radius of your circle? - "))
def calculate_area(radius):
    pi = 3.14
    area = pi * (radius ** 2.0)
    print("The area of your circle is",area)
    return area

print(calculate_area(radius))
'''
"""
original_list = [2,7,10]

def swap_first_last(list):
    temp = list[2]
    list[2] = list[0]
    list[0] = temp 
    print(list)

modified_list = swap_first_last(original_list)
print(modified_list)
"""
