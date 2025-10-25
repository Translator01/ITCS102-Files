name = input("Input your name here ---> ")
print("Hi", name, "Welcome to the ODD NUMBER SUMMATION PROGRAM")
print("Mechanics: You may enter random number. Then, press 0 if you want the program to stop\n")

num = True

sum = 0

odd = " "

while num == True:
    val = eval(input("Input any number: "))

    if val % 2 == 1:
        print("Odd Number Detected, proceed to next number ")
        sum += val
        odd += str(val) + " "
        continue
    elif  val == 0:
        print("Program stops. ")
        break

    else:
           if val % 2 == 0:
               print("Even Number Detected, proceed to next number ")
           else:
                print("Invalid")
                continue
print(f"Hi {name}, the total sum of all odd numbers is {sum}")
print(f"ODD numbers detected {odd}")                