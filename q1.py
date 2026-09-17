
import math

while True:
    choice = input("\nEnter operation (+, -, /, ! for factorial) or 'exit': ")

    if choice == "exit":
        print("Calculator terminated.")
        break

    if choice == "!":
        n = int(input("Enter a number: "))
        print("Factorial =", math.factorial(n))

    elif choice in ["+", "-", "/"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "+":
            print("Result =", a + b)

        elif choice == "-":
            print("Result =", a - b)

        elif choice == "/":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)

    else:
        print("Invalid choice")