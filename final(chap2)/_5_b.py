""" Compute the area and circumference of
a circle given the radius r if the radius is
greater than or equal to 1.0; otherwise, you
should compute only the circumference. """

import math

r = float(input("Enter the radius of circle: "))

if r>=1.0:
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r

    print("The area of this circle is ", area)
    print("The circumference of this circle is ", circumference)

else: 
    circumference = 2 * math.pi * r

    print("The circumference of this circle is ", circumference)