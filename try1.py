balance = 20000
try:
    amount = float(int(input("Enter a withdrawal amt")))

    if amount <= 0:
        raise ValueError("Amt must be positive")

    if amount > balance:
        raise Exception("Insufficient bal")

    balance -= amount

    print("success")
    print("remaining")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)