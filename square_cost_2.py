""" Write an algorithm that inputs the length and width, in feet, of a
rectangular carpet and the price of the carpet in dollars per square yard. It
then determines if you can afford to purchase this carpet, given that your
total budget for carpeting is $500 """

length = float(input("Please enter length: "))
width = float(input("Please enter width: "))
price = float(input("Please enter the price: "))

area = (length / 3) * (width / 3)
cost = area * price

if (cost <= 250):
    print("This is a particularly good deal.")
elif (cost <= 500):
    print("You can afford to purchases this carpet.")
else:
    print("You can't afford to purchases this carpet.")