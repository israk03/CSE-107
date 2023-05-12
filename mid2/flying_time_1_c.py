""" Determine the flying time between two
cities given the mileage M between them
and the average speed of the airplane. """

def flying_time(d,s):
    time = d/s
    return time

distance = float(input("Distance: "))
speed = float(input("Speed: "))

time = flying_time(distance, speed)

print(f"Flying time is {time} hours.")