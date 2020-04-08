a = 5
b = 0

try:
    print("open")
    print (a/b)
    k = int(input('Enter any number : '))
    print (k)

except ZeroDivisionError as e:
    print("can't divide by zero :", e)

except ValueError as e:
    print("k should be integer :", e)

except Exception as e:
    print('Something went wrong.')

finally:
    print ("close")
    print ("bye")


