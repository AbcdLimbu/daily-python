try:
    x = 1/2
    y = int("John")
    print(x)

except (ZeroDivisionError,ValueError) as e:
    print(e)

finally:
    print("Kya baat hai")
