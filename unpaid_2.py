""" Write an algorithm that gets as input your current credit card balance,
the total dollar amount of new purchases, and the total dollar amount of
all payments. The algorithm computes the new balance, which this time
includes an 8% interest charge on any unpaid balance below $100, 12%
interest on any unpaid balance between $100 and $500, inclusive, and 16%
on any unpaid balance above $500. """

balance = float(input("Enter your current credit card balance: "))
purchases = float(input("Enter the amount of new purchases: "))
payment = float(input("Enter amount of all payments: "))

unpaid_balance = balance - (purchases + payment)

if (unpaid_balance < 0):
    interest = 0
elif (unpaid_balance < 100):
    interest = 0.08
elif (unpaid_balance <= 500):
    interest = 0.12
else:
    interest = 0.16

new_balance = unpaid_balance + unpaid_balance * interest

print("The new balance is ", new_balance)