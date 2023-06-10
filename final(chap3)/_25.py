""" Consider the following sorted list of names.
Arturo, Elsa, JoAnn, John, José, Lee, Snyder, Tracy
a. Use binary search to decide whether Elsa
is in this list. What names will be compared
with Elsa? """

names = ["ami", "tumi", "elsa"]
target = "tumi"

low = 0
high = len(names) - 1
found = False

while (low <= high):
    mid = (low+high) // 2
    mid_name = names[mid]

    if mid_name == target:
        found = True
        break
    elif mid_name < target:
        low = mid + 1
    else: 
        high = mid - 1


if found:
    print(f"{target} found")

else: 
    print("not found")