""" An algorithm that gets the radius r of a circle as input.
Its output is both the circumference and the area of a circle of radius r. """

import math

r = int(input("Please enter a radius: "))

c = 2 * math.pi * r
area = math.pi * r * r
square_root = math.sqrt(r)

print("Circumference of this circle is ",c)
print("The area of this circle is ", area)
print("The square root of this circle is ", square_root)