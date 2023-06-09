""" For each of the following lists, perform a bubble
sort, and show the list after each exchange.
.

c. D, B, G, F, A, C, E, H """

list_c = ['D', 'B', 'G', 'F', 'A', 'C', 'E', 'H']
n = len(list_c)

for i in range(n-1): 
    for j in range(n-i-1): 
        if list_c[j] > list_c[j+1]: 
            list_c[j], list_c[j+1] = list_c[j+1], list_c[j]

    print(f"step {i+1}: {list_c}")

print("sorted list: ", list_c)
