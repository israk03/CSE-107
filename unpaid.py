""" An algorithm that inputs your #current credit card balance, the total dollar
amount of #new purchases, and the total dollar amount of #all payments. The
algorithm computes the new balance, which includes a 12% interest charge
on any unpaid balance. """

current_balance = int(input("Please enter your current balance: "))
new_purchases = int(input("Please enter your amount of new purchases: "))
total_payments = int(input("Please enter your total payments: "))

unpaid_balance = (current_balance - total_payments)

new_balance = (unpaid_balance + (unpaid_balance * .12) + new_purchases)

print(new_balance)