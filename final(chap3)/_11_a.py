""" For each of the following lists, perform a bubble
sort, and show the list after each exchange.
.
a. 4, 8, 2, 6
"""

list_a = [4, 8, 2, 6]
n = len(list_a)

for i in range(n-1):
    for j in range(n-i-1):
        if list_a[j] > list_a[j+1]:
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]

    print(f"step {i+1}: {list_a}")

print("sorted list: ", list_a)