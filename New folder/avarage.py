""" Write an algorithm that gets as input three data values x, y, and z and
outputs the average of these values if the value of x is positive. If the value
of x is either 0 or negative, your algorithm should not compute the average
but should print the error message ‘Bad Data’ instead. """

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))

if x > 0:
    average = (x + y + z) / 3
    print("The average of x, y, and z is:", average)
else:
    print("Bad Data")
