""" Compute the interest earned in 1 year given
the starting account balance B and the annual
interest rate I and assuming simple interest,
that is, no compounding. Also determine the
final balance at the end of the year. """

B = float(input("Enter the starting account balance: "))
I = float(input("Enter the annual interest rate: "))

interest = B * I
final_balance = B + interest

print(f"Interest earned in one year: {interest:.2f}")
print(f"Final balance at the end of the year: {final_balance:.2f}")