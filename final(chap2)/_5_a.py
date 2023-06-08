""" Compute and display the value x ÷ y if the
value of y is not 0. If y does have the value 0,
then display the message ‘Unable to perform
the division’. """

x = float(input("enter the value of x = "))
y = float(input("enter the value of y = "))

if y!=0:
    ans = x/y
    print("the answer of this division is ", ans)
else: 
    print("unable to perform this division.")