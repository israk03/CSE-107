""" For each of the following lists, perform a bubble
sort, and show the list after each exchange.
.

b. 12, 3, 6, 8, 2, 5, 7
"""

list_b = [12, 3, 6, 8, 2, 5, 7]
n = len(list_b)

for i in range(n-1):
    for j in range(n-i-1): 
        if list_b[j] > list_b[j+1]:
            list_b[j], list_b[j+1] = list_b[j+1], list_b[j]

    print(f"step {i+1}: {list_b}")

print("sorted list: ", list_b)