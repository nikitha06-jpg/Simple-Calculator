

print("===== Simple Calculator =====")
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, %, **, //): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed"
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Modulus by zero is not allowed"

elif operator == "**":
    result = num1 ** num2

elif operator == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Error: Floor division by zero is not allowed"

else:
    result = "Invalid operator"
print("Result:", result)
