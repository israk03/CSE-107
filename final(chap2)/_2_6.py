""" write an algorithm that gets
values for the starting account balance B,
annual interest rate I, and annual service
charge S ((the annual service charge only if the starting
account balance at the beginning of the year
is less than $1,000. If it is greater than or equal
to $1,000, then there is no annual service
charge.)). Your algorithm should output the
amount of interest earned during the year
and the final account balance at the end of
the year. Assume that interest is compounded
monthly and the service charge is deducted
once, at the end of the year. """

B = float(input("Enter the starting account balance: "))
I = float(input("Enter the annual interest rate: "))
if B < 1000:
    S = float(input("Enter the annual service charge: "))
else: 
    S = 0

monthly_interest = I/12
interest_earned_month = B * monthly_interest
total_interest = 0

for i in range(12):
    total_interest += interest_earned_month
    B += interest_earned_month
if B < 1000: 
    B -= S

print("The amount of interest earned during the year: ", total_interest)
print("The final account balance at the end of the year: ", B)