#Making a function called space to not repeat code
def space():
    print("-------------------------")


space()
#Checking if input value is an Integer
while True:
    try:
        number = int(input("Number Range: "))
        break
    except ValueError:
        print("Error can only input numbers")

    
#You can chose Odd or Even
user = input("Odd | Even: ")
space()

#Adding plus one because it always starts counting at 0
number = int(number) + 1

#Print the chosen number rang and the Odd or Even Numbers
for i in range(number):
    if user.lower() == "even":
        if i % 2 == 0:
            print(i)
    elif user.lower() == "odd":
        if i % 2 > 0:
            print(i)
    else:
        print("Error")
space()