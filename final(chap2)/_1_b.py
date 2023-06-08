""" 
Compute the interest earned in 1 year given
the starting account balance B and the annual
interest rate I and assuming simple interest,
that is, no compounding. Also determine the
final balance at the end of the year. """

B = float(input("Please enter the starting account balance: "))
I = float(input("Please enter the annual interest rate: "))

interest_earned = (B*I)/100
final_balance = B + interest_earned

print("Interest earend in one year: ",interest_earned)
print("Final balance: ",final_balance)