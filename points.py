""" An algorithm that is given three numbers corresponding to the number of
times a race car driver has finished first, second, and third. The algorithm
computes and displays how many points that driver has earned given 5
points for a first, 3 points for a second, and 1 point for a third place finish. """

a = int(input())
b = int(input())
c = int(input())

total_points = (a*5) + (b*3) + (c*1)

print("total points",total_points)