# finally block
try:
    num=int(input("enter number:"))
    result=50/num
except ZeroDivisionError:
    print("division by zero is not allowed") 
      
finally:
    print("this is finally block")