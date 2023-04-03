''' Write an if/then/else statement that sets the variable y to the value 1 if
x ≥ 0. If x < 0, then the statement should set y to the value 2. (Assume x
already has a value.)'''

x = int(input())

if x>=0:
    y = 1
else:
    y = 2

print("Y =", y)