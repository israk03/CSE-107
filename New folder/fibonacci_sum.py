n = int(input())

a, b = 0, 1
sum = 0
for i in range(n):
   
    sum = sum + a
    result = a + b
    a = b
    b = result
print(sum)