""" Write an algorithm that gets as input a single nonzero data value x and
outputs the three values x2, sin x, and 1/x. This process is repeated until the
input value for x is equal to 999, at which time the algorithm terminates.
Assume the input for the data value x can be any value, including 0.
Since the value 1/x cannot be computed if x = 0, you will have to check for
this condition and output an error message saying that you are unable to
compute the value 1/x. """

import math
while True:
    x = float(input("Enter a non zero value (999 for exit): "))

    if (x==999):
        break
    else:
        x_squared = x**2
        sin_x = math.sin(x)
        if(x==0):
            print("you are unable to compute.")
        else:
            one_by_x = 1 / x

            print(f"x2 =", x_squared)
            print(f"sin x=", sin_x)
            print(f"1/x=", one_by_x)