""" Write a code that is given your electric
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
    initial_reading = float(input(f"Enter the initial meter reading for the month {month}:"))
    final_reading = float(input(f"Enter the final meter reading for the month {month}:"))

    kwh_used = final_reading - initial_reading

    if kwh_used<=1000:
        cost = kwh_used * 0.06
    else:
        cost = (1000 * 0.06) + ((kwh_used - 1000) * 0.08)

    total_cost += cost
    total_kwh += kwh_used

print(f"The annual cost of electricity is {total_cost}")

if total_kwh < 500:
    print("Thank you for conserving electricity.")