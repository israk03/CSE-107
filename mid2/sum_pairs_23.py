""" Design and implement an algorithm that gets
as input a list of k integer values N1, N2, . . ., Nk
as well as a special value SUM. Your algorithm
must locate a pair of values in the list N that
sum to the value SUM. For example, if your
list of values is 3, 8, 13, 2, 17, 18, 10, and the
value of SUM is 20, then your algorithm would
output either of the two values (2, 18) or
(3, 17). If your algorithm cannot find any pair
of values that sum to the value SUM, then it
should print the message ‘Sorry, there is no
such pair of values’. """

def find_pair_sum(numbers, SUM): 
    hash_table = {}
    for num in numbers: 
        diff = SUM - num
        
        if diff in hash_table: 
            return (diff,num)
        hash_table[num] = True

    print("Sorry there are no pair.")

numbers = list(map(int, input("Please enter values: ").split()))
SUM = int(input("Please enter target sum: "))

pair = find_pair_sum(numbers, SUM)

if pair: 
    print(pair)