""" Modify the sales computation algorithm
of Exercise 4 so that after finishing the
computation for one item, it starts on the
computation for the next. This iterative process
is repeated until the total cost exceeds $1,000. """

total_cost = 0

while(total_cost<=1000):
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))

    sub_total = price * quantity
    tax = sub_total * 0.06
    cost = sub_total + tax

    print(f"Total cost of the item is ${cost}, with 6% tax.")

    total_cost += cost

print("total cost exceeds $1000")