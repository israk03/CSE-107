n = int(input())

a, b = 0, 1

for i in range(n):
    print(a, end = " ")

    result = a + b
    a = b
    b = result
    