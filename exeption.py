# else block and finally block
try:
    num=int(input("enter number:"))
    result=50/num
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("invalid input")
else:
    print("result is:", result)
finally:
    print("this is finally block")
