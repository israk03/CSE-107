NUMBER = input("Enter the number you want to search: ")
T = []
N = []
for i in range(10000):
    T.append(input("Enter the {}th number on the list: ".format(i+1)))
    N.append(input("Enter the corresponding person's name: "))
i = 0
Found = False
while not Found and i < 10000:
    if NUMBER == T[i]:
        print("The corresponding person is:", N[i])
        Found = True
    else:
        i += 1
if not Found:
    print("Sorry, this number is not in the directory")
