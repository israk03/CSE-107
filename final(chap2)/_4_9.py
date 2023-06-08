""" Write an algorithm that gets the price for item
A plus the quantity purchased. The algorithm
prints the total cost, including a 6% sales tax.

Modify the sales computation algorithm
of Exercise 4 so that after finishing the
computation for one item, it starts on the
computation for the next. This iterative process
is repeated until the total cost exceeds $1,000."""

total_cost = 0

while(total_cost<=1000):
    p = float(input("Enter the price of the item: "))
    q = float(input("Enter the quantity of the item: "))

    sub_total = p * q
    tax = sub_total * 0.06
    total = sub_total + tax

    print(f"Total cost of this item is ${total}, including 6% tax.")

    total_cost += total

print("The total cost exceeds $1000.")
