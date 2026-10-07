numbers= list(range(1, 101))
for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        print ('FizzBuzz')
    elif number % 3 == 0:
        print ('FIZZ')
    elif number % 3 == 0:
        print ('BUZZ')
    else:
        print (number)