#print 1 to 100 number in turn
#when number is divisible by 3 then insted of printing the number it should print 'FIZZ'
##when number is divisible by 5 then insted of printing the number it should print 'BUZZ'
#And when number is divisible by 3 and 5 then insted of printing the number it should print 'FIZZBUZZ'

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)