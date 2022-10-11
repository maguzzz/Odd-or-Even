from tokenize import Number


print("-------------------------")
number = input("Number Range: ")

print("Odd | Even\n")
user = input()

#Print the chosen number rang and the Odd or Even Numbers
for i in range(int(number)):
    if user == "Even":
        if i + 1 % 2 == 0:
            print(i)
    elif user == "Odd":
        if i + 1 % 2 > 0:
            print(i)
    else:
        print("Error")
        