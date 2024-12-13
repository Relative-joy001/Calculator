# Python weight calculator

weight = float(input("Enter your weight: "))

unit = input("kilograms or Pounds ( k or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is:{round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is:{round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

