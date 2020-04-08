print('BUILD A RIGHT ANGLE TRIANGLE')
i = 1
size = int(input('SIZE: '))
while i<=size:
    print ('*'* i)
    i+=1
print ("YAAYYYY....WELL DONE")
print()

print('GUESS THE NUMBER GAME  ????')
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('GUESS : '))
    guess_count+=1
    if guess == secret_number:
        print('YOU WON!!!')
        break
    elif guess_count != (guess_limit-1):
        print('WRONG GUESS, TRY AGAIN') 
    else:
        print ('LAST TRY')
       
else:
    print('SORRY YOU LOOSE :-( ')

print()
print('GET THE SUM......')
print ('NOTE: enter -1 in the end of the list')
print('Enter Prices:')
total = 0
while True:
    price = int(input('> '))
    if price == -1:
        break
    total += price
print (f'TOTAL IS {total}')
print()


print ("PRINTING 'F' PATTERN")
numbers = [5,2,5,2,2]

for x in numbers:
    output = ''
    for  y in range(x):
        output += 'X'
    print (output)



input('       ........Programme ends.....  ')