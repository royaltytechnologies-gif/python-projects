print ('Good day , Esteemed Player')
print ('you are wellcomed aboard this game of EVEN or ODD')
x= input ('Will you like to proceed with the game? type YES to continue or NO to quit  ')
while x != 'YES' and x != 'NO' and x != 'yes' and x != 'no':
    print ('Invalid answer')
    x = input ('Please type yes or no to continue   ')
if x == 'YES' or x == 'yes':
    print('Alright. ')
    num = int(input('Pick a ramdom number   '))
    if num % 2 ==0:
        print (F'{num} is Even')
    elif num % 2 == 1:
        print (F'{num} is ODD')
elif x == 'NO' or x == 'no': 
    print ('Alright, Have a good day')
else : 
    print ('Invalid Answer')

    