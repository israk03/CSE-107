""" Write an algorithm that gets the price for item
A plus the quantity purchased. The algorithm
prints the total cost, including a 6% sales tax.

ALGORITHM:
1. Input the price of the item (P) and the quantity purchased (Q)
2. Multiply P by Q to get the subtotal (S)
3. Multiply S by 0.06 to get the sales tax (T)
4. Add T to S to get the total cost (C)
5. Print "The total cost of the item is $C, including a 6% sales tax."
"""

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

sub_total = price*quantity
tax = sub_total * 0.06
cost = sub_total + tax

print(f"The total cost of the item is {cost}, includeing 6% tax.")