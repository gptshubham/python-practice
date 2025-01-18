# import math
#
# result = math.pow(5,2)
# print(result)

# from math import *
# result = pow(2,5)
# print(result)
#
# result = sqrt(16)
# print(result)

import math as m
print(m.pi)
print(m.factorial(5))
print(m.floor(10.9))
print(m.ceil(10.1))

# calculating area of circle
r = int(input('Enter radius of the circle: '))
area = round(m.pi * (r**2), 2)
print(f'The Area of the Circle is: {area} square unit')