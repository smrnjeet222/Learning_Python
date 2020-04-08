smaller_number =10
bigger_number = 20
result = smaller_number == bigger_number
print(result)
result = smaller_number != bigger_number
print (result)
result = smaller_number >= bigger_number and smaller_number == bigger_number   # like &&
print (result)
result =  not smaller_number > bigger_number
print (result)
result = smaller_number == bigger_number or smaller_number <= bigger_number  # like ||
print (result)


if bigger_number == smaller_number :
    print ("bigger_number is bigger")
elif bigger_number <= smaller_number:
    print ("smaller_number is bigger")

elif bigger_number != smaller_number:
    print ("smaller_number is not equal")    
else:
    print("false")

if bigger_number <= smaller_number :
    print ("bigger_number is bigger.")
else:
    print("false")
print ("programme ends")   









input('     .......Programme ends.....   ')