print("Welcome to the odd number summation program!")

total = 0
for i in range(7):
    num = int(input("Enter a number:  "))
    if num % 2 != 0:
        total += num
print("Sum of odd numbers entered:", total)

