print("🦜 Parrot Simulator - The Echo Chamber")

say = input("What would you like the parrot to say? ")
num = int(input("How many times should the parrot repeat it? "))
for _ in range(num):
    print("🦜 Squawk!", say)