import re 

message = "call me at 9999222444"

phone_no = re.compile(r'(\d\d-)?\d\d\d\d\d\d\d\d\d\d')

mo = phone_no.search(message)

print (mo)


batregrex = re.compile(r'bat{|man|car|mobile|copter}')
mo = batregrex.search ('batman is awesome.')

print (mo)


batregrex = re.compile(r'Bat(wo)?man')   # ? is 0 or 1 times
mo =  batregrex.search('Batwoman is lit')

print (mo)

googleregrex = re.compile(r'Go(o)*gle')  # * is zero or more times

print(googleregrex.search('Goooooooogle'))
print(googleregrex.search('Google'))
print(googleregrex.search('Gogle'))

googlenewregrex = re.compile(r'Go(o)+gle') # + is one or more times

print(googlenewregrex.search('Gogle')) # returns NONE 
print(googleregrex.search('Goooooooogle'))

gogregrex = re.compile(r'g(o){2}gle') # repeat o 2 times 

print ( gogregrex.search('google is easy. not goooooogle'))


