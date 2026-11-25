#apssword validation program
try:
    password=input("Enter your password:")
    if len(password)<8:
        raise ValueError("Password must be at least 8 characters long")
    if not password.isalpha():
        raise ValueError("must contain alphapbets")
    print("Password is valid")
except ValueError as e:
    print("Error:", e)