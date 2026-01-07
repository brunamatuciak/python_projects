

def Calculator():

    print("This is a simple calculator.")

    number1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    number2 = float(input("Enter the second number: "))

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        print("Invalid operator.")
        return

    print(f"The result is: {result:.2f}")


Calculator()
