""" An algorithm that is given the length and width, in feet, of a rectangular carpet
and determines its total cost given that the material cost is $23 per square yard. """

lenth = int(input("please enter lenth: "))
width = int(input("please enter width: "))

area = (lenth * width) / 9
cost = area * 23

print("total cost, ", cost)