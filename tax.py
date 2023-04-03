""" An algorithm that gets the amount of electricity used in kilowatt-hours and
the cost of electricity per kilowatt-hour. Its output is the total amount of the
electric bill, including an 8% sales tax. """

kw = int(input("Electricity used in kilowatt hours: "))
cost = int(input("Cost per killowatt: "))

total_cost = kw * cost
tax = (8*total_cost) / 100

total_bill = total_cost + tax

print(total_bill)