""" Use the binary search algorithm to decide
whether 35 is in the following list:
3, 6, 7, 9, 12, 14, 18, 21, 22, 31, 43 """


nums = [3, 6, 7, 9, 12, 14, 18, 21, 22, 31, 43]
target = 3

left = 0
right = len(nums) - 1
found = False

while(left<=right):
    middle = (left+right) // 2

    if nums[middle] == target:
        found = True
        break
    elif nums[middle] < target: 
        left = middle + 1
    else:
        right = middle - 1

if found: 
    print("Target numbers found at index: ", middle)
else: 
    print("Target not found")