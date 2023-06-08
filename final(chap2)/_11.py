""" Develop an algorithm to compute gross pay.
The inputs to your algorithm are the hours
worked per week and the hourly pay rate.
The rule for determining gross pay is to pay
the regular pay rate for all hours worked up
to 40, time-and-a-half for all hours over 40 up
to 54, and double time for all hours over 54.
Compute and display the value for gross pay
using this rule. After displaying one value,
ask the user whether he or she wants to do
another computation. Repeat the entire set of
operations until the user says no. """

repeat = True
while repeat: 
    hours_worked = float(input("enter the hours worked per week: "))
    pay_rate = float(input("enter the hourly pay rate: "))

    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate

    elif hours_worked <= 54:
        regular_pay = 40 * pay_rate
        over_time = hours_worked - 40
        over_time_pay = over_time * 1.5 * pay_rate
        gross_pay = regular_pay + over_time_pay

    else: 
        regular_pay = 40 * pay_rate
        over_time_pay = 14 * 1.5 * pay_rate
        double_time_hours = hours_worked - 54
        double_time_pay = double_time_hours * 2 * pay_rate
        gross_pay = regular_pay + over_time_pay + double_time_pay

    print("The gross pay is ",gross_pay)

    repeat_again = input("Do you want to continue? (yes/no?): ")
    if repeat_again.lower() == "no":
        repeat = False