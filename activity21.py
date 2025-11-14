clothes = True

while clothes == True:
    isDirty = input("Is the clothes clean? (yes/no): ").lower()
    if isDirty == 'no':
        print("Washing Continues")
        continue
    else:
        print("Your clothes is clean")
        break