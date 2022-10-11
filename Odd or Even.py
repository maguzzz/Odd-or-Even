print("-------------------------")
number = input("Number Range: ")
#Adding a 1 because if user enters 10 it would only count up to 9
number = int(number) + 1
#You can chose Odd or Even
user = input("Odd | Even: ")
print("-------------------------")

#Print the chosen number rang and the Odd or Even Numbers
for i in range(number):
    if user == "Even":
        if i % 2 == 0:
            print(i)
    elif user == "Odd":
        if i % 2 > 0:
            print(i)
    else:
        print("Error")
        