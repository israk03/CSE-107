""" Design and implement an algorithm that is
given as input an integer value k ≥ 0 and a list
of k numbers N1, N2, . . ., Nk. Your algorithm
should reverse the order of the numbers in the
list. That is, if the original list contained:
N1 = 5, N2 = 13, N3 = 8, N4 = 27, N5 = 10
(k = 5)
then when your algorithm has completed, the
values stored in the list will be:
N1 = 10, N2 = 27, N3 = 8, N4 = 13, N5 = 5 """

def reverse_list(nums):
    return nums[::-1]

k = int(input("Please enter the list size: "))

nums = []

for i in range(k):
    while True:
        try:
            n = int(input(f"Enter the value of list: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    nums.append(n)

listt = reverse_list(nums)

print(listt)
