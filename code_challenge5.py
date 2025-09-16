print("Welcome to the factorial calculator!")
num = int(input("Enter any number here:  "))
fact = 1
for i in range(num, 0, -1):
    fact *= i
print(f"The factorial of {num} is {fact}")
