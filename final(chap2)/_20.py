""" Design an algorithm that is given a positive
integer N and determines whether N is a
prime number, that is, not evenly divisible by
any value other than 1 and itself. The output
of your algorithm is either the message
‘not prime’, along with a factor of N, or the
message ‘prime’. """

import math

def is_prime(n):

    if n<=1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

a = int(input("Enter a integer number: "))

if is_prime(a):
    print("prime")
else: 
    print("not prime")