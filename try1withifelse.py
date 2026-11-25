# withdrawal program
# using else and finally block

balance=20000
try:
    amount = float(input("Enter withdrawal amount:"))
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
    print("Withdrawal successful...")
except ValueError as e:
    print("Error:", e)
else:
    print("No exceptions occurred.")
finally:
    print("Withdrawal process completed.")
    print("Remaining balance:", balance)