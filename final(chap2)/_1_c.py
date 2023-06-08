""" 
Determine the flying time between two
cities given the mileage M between them
and the average speed of the airplane. """

d = float(input("Enter the distance between two cities: "))
s = float(input("Enter the speed of the airplane: "))

time = d/s

print("Flying time is:",time,"hours.")