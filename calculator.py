# Python Calculator
operator =input("Enter an operator (+ - / *  % ): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
# result = num1 operator num2

if operator=="+":
    result = num1 + num2
    print(f"The result is: {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {round(result, 2)}")

elif operator == "/":
    result = num1 / num2
    print(f"The result is: {round(result, 2)}")

elif operator == "*":
    result = num1 * num2
    print(f"The result is: {round(result, 2)}")

elif operator == "%":
    result = num1 % num2
    print(f"The result is: {round(result, 2)}")
else:
    print(f"Your {operator} is invalid operator!")


