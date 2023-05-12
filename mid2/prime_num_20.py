""" Design an algorithm that is given a positive
integer N and determines whether N is a
prime number, that is, not evenly divisible by
any value other than 1 and itself. The output
of your algorithm is either the message
‘not prime’, along with a factor of N, or the
message ‘prime’. """

import math

def is_prime(n):
    if n<2:
        return "not prime"
    elif n == 2:
        return "prime"
    elif n % 2 == 0:
        return "not prime",2
    
    sqrt_n = int(math.sqrt(n)) + 1

    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return "not prime",i
        else: 
            return "prime"
        
a = int(input("Enter a positive integer: "))

res = is_prime(a)

print(res)