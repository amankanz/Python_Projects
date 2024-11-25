# Python Temp Converter
unit = input("Is the Temp in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the Temp: "))

if unit == "C":
    result = (temp * 9/5) + 32
    print(f"The temp in Fahrenheit is : {result}F")
elif unit == "F":
    result = (temp - 32) * 5/9
    print(f"The temp in Celsius is : {result}C")
else:
    print(f"The {unit} is an invalid unit of measurement! ❌")