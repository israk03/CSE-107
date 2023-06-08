""" write an algorithm that gets
values for the starting account balance B,
annual interest rate I, and annual service
charge S. Your algorithm should output the
amount of interest earned during the year
and the final account balance at the end of
the year. Assume that interest is compounded
monthly and the service charge is deducted
once, at the end of the year. """

B = float(input("Enter the starting account balance: "))
I = float(input("Enter the annual interest rate: "))
S = float(input("Enter the annual service charge: "))

monthly_interest = I / 12
interest_earned_month = monthly_interest * B
total_interest = 0

for i in range(12):
    total_interest += interest_earned_month
    B += interest_earned_month

B -= S

print(f"Interest earned during the year {total_interest:.2f}")
print(f"Total balance {B:.2f}")



""" write an algorithm that gets
four numbers corresponding to scores received
on three semester tests and a final examination.
Your algorithm should compute and display
the average of all four tests, weighting the final
exam twice as heavily as a regular test. """

s1 = float(input("Enter marks for test 1: "))
s2 = float(input("Enter marks for test 2: "))
s3 = float(input("Enter marks for test 3: "))
s4 = float(input("Enter marks for final: "))

average = ((s1+s2+s3)/3)*0.4 + (s4*0.6)

print("The average for all four tests is: ", average)



""" Compute and display the value x ÷ y if the
value of y is not 0. If y does have the value 0,
then display the message ‘Unable to perform
the division’. """

x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

if y!=0: 
    r = x/y
    print(r)
else: 
    print("unable to division.")




""" Compute the area and circumference of
a circle given the radius r if the radius is
greater than or equal to 1.0; otherwise, you
should compute only the circumference """

import math

r = float(input("please enter the radius: "))

if r>=1: 
    a = math.pi * r ** 2
    c = 2 * math.pi * r
    print("The area is : ", a)
    print("the circ... is: ",c)
else: 
    c = 2 * math.pi * r 
    print("The circu.... is: ", c)




""" Modify the test-averaging algorithm of
Exercise 3 so that it reads in 15 test scores
rather than 4. There are 14 regular tests and a
final examination, which counts twice as much
as a regular test. Use a loop to input and sum
the scores. """

num_test = 15 
regular_test = num_test - 1
test_score = 0

for i in range(regular_test):
    score = float(input(f"Enter the score for test {i+1}: "))
    test_score += score

final = float(input("Enter the final test score: "))

test_average = test_score / regular_test
average = (test_average * 0.4) + (final * 0.6)

print(average)




""" Write an algorithm that is given your electric
meter readings (in kilowatt-hours) at the
beginning and end of each month of the year.
The algorithm determines your annual cost of
electricity on the basis of a charge of 6 cents
per kilowatt-hour for the first 1,000 kilowatt-hours
of each month and 8 cents per kilowatt-
hour beyond 1,000. After printing out your total
annual charge, the algorithm also determines
whether you used less than 500 kilowatthours
for the entire year and, if so, prints out a
message thanking you for conserving electricity. """

total_kwh = 0
total_cost = 0

for month in range(1,13): 
    initial_reading = float(input(f"enter the initial meter reading for month {month}: "))
    final_reading = float(input(f"enter the final meter reading for month {month}: "))

    kwh_used = final_reading - initial_reading

    if kwh_used <= 1000:
        cost = kwh_used * 0.06

    else: 
        cost = (1000*0.06) + ((kwh_used - 1000) * 0.08)

    total_kwh += kwh_used
    total_cost += cost

print("The annual electricity cost : ", total_cost)

if total_kwh < 500:
    print("thank you")
