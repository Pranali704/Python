# exception object

try:
    a=10/0
except ZeroDivisionError as e:
    print("Exception message:", e)