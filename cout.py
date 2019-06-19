# Python program showing how to use 
# string modulo operator(%) to print 
# fancier output 

# print integer and float value 
print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.3353)) 

# print integer value 
print("Total students : % 3d, Boys : % 2d" %(240, 120)) 

# print octal value 
print("% 7.3o"% (25)) 

# print exponential value 
print("% 10.3E"% (356.08977)) 

#NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW......METHOD

# Python program showing 
# a use of format() method 

# combining positional and keyword arguments 
print('\nNEW\nNumber one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks')) 

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}". 
	format(12, 00.546)) 

# Changing positional argument 
print("Second argument: {1:3d}, first one: {0:7.2f}". 
	format(47.42, 11)) 

print("Geeks: {a:5d}, Portal: {p:8.2f}". 
	format(a = 453, p = 59.058)) 

#NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW......METHOD

# Python program to 
# format a output using 
# string() method 

cstr = "I love geeksforgeeks"
	
# Printing the center aligned 
# string with fillchr 
print ("\n\nCenter aligned string with fillchr: ") 
print (cstr.center(40, '#')) 

# Printing the left aligned 
# string with "-" padding 
print ("\n\nThe left aligned string is : ") 
print (cstr.ljust(4, '-')) 

# Printing the right aligned string 
# with "-" padding 
print ("\n\nThe right aligned string is : ") 
print (cstr.rjust(40, '-')) 

#NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW......METHOD

# Python program to 
# show format () is 
# used in dictionary 

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 

# using format() in dictionary 
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
	'Geeks: {0[geek]:d}'.format(tab)) 

data = dict(fun ="GeeksForGeeks", adj ="Portal") 

# using format() in dictionary 
print("I love {fun} computer {adj}".format(**data)) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)