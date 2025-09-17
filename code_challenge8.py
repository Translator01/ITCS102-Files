print("Multiplication Table Maker")
num = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")