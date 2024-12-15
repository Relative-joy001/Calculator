# temp convertor

unit = input("Is this temperature in celsius or fahrenheit (C/F): ")
temp = float(input("Enter your temperature: "))

if unit == "F":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperaturen in fahrenheit is : {temp} f")
elif unit == "C":
    temp = round((temp - 32) * 5 / 32, 1)
    print(f"The temperaturen in celsius is : {temp} c")
else:
    print(f"{unit} is an invalid unit of measurement")
