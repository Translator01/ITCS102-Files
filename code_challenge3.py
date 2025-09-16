name = input("Enter your name: ")
fare = eval(input("Enter the fare: "))
studentID = input("Are you a student? (yes/no): ").strip().lower()

if studentID == "yes":
    discount = fare * 0.20
    new_discount = fare - discount
    print(f"Thank you {name}! Your final fare is: {new_discount}")
else:
    print("Sorry you are not eligible for a student discount.")
    print(f"Your fare is: {fare}")