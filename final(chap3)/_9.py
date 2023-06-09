""" Perform a selection sort on the list 7, 4, 2, 9, 6.
Show the list after each exchange that has an
effect on the list ordering. """

numbers = input("Please enter a list of numbers: ").split()
numbers =[int(num) for num in numbers]      # numbers = [7,4,2,9,6]
print("Original list: ", numbers)

length = len(numbers)

for i in range(length - 1):
    for j in range(length - i - 1): 
        if numbers[j] > numbers[j+1]: 
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f"step {i+1}: {numbers}")

print("Sorted list: ", numbers)