months = ["jan", "feb", "mar", "apr", "may", "jun", "jul"]


months.append("aug")
print(months)


months.pop()
print(months)

months.remove("mar")
print(months)

months.insert(4, "new")
print(months)

list = len(months)
print("Length of list:", list)

months.sort()
print("Sorted list:", months)

for m in months:
    print(f"{m},2025")


fullname = 'Donn Romuelle B. Balmaceda'

# #list slicing / reverse name

print(fullname[::-1])