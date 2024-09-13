# This programm will convert between F and C.

print("It's raining like a hell.\n")

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))
last_temp = temp
if unit == "C" or unit == "c":
    temp = round((9*temp)/5 + 32, 1)
    print(f"{last_temp} °C is equal to {temp} °F")
elif unit == "F" or unit == "f":
    temp = round((temp-32)*5/9, 1)
    print(f"{last_temp} °F is equal to {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement")
    