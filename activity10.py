name = input("whast your name?:")
student = input("are you a student (Yes / No)?:")
fare = eval(input("money pls:"))

if student.lower() == "yes" :
	discount = fare * .2
	new_fare = fare - discount
	print("Hi, name","student discount is", discount, "Discount fare is", new_fare)
else:
	print("Sorry you are not a student so no discount")SD