temp = eval(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Temperature is below freezing point.")
elif temp >= 1 and temp <= 15:
    print("Temperature is Extremely Cold.")
elif temp >= 16 and temp <= 30:
    print("Temperature is Cold.")
elif temp >= 31 and temp <= 38:
    print("Temperature is Lukewarm.")
elif temp >= 39 and temp <= 42:
    print("Temperature is Warm.")
elif temp >= 43 and temp <= 50:
    print("Temperature is Hot.")
elif temp >= 51 and temp <= 60:
    print("Temperature is Extremely Hot.")
elif temp > 60:
    print("Temperature is Burning.")
else:
    print("Invalid temperature input.")