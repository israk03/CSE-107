""" write a python code without def function and
use user input to find the median value in a list
containing N unique numbers. The median of N numbers
is defined as the value in the list in which approximately
half the values are larger than it and half
the values are smaller than it. For example,
consider the following list of seven numbers.
26, 50, 83, 44, 91, 20, 55
The median value is 50 because three values
(20, 26, and 44) are smaller and three values
(55, 83, and 91) are larger. If N is an even
value, then the number of values larger than
the median will be one greater than the
number of values smaller than the median.

 """

n = int(input("enter the numbers of element: "))
num = []

for i in range(n):
    numbers = int(input(f"enter the number {i+1}: "))
    num.append(numbers)

num.sort()

if n%2==0:
    mid1 = n//2
    mid2 = mid1 - 1
    median = (num[mid1]+num[mid2])/2

else:
    mid = n//2
    median = num[mid]

print("Median: ", median)