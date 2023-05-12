""" Compute and display the value x ÷ y if the
value of y is not 0. If y does have the value 0,
then display the message ‘Unable to perform
the division’. """

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

if y!= 0: 
    result = x / y
    print("x/y = ", result)
else: 
    print("Unable to perform the division.")