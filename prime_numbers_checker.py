from factorial_calculator import factorial

def isPrime(int):
    if int == 1:
        return False
    else:
        if factorial(int-1)%int == (int-1):
            return True
        else: return False

while True:
    try:
        integer = int(input('Enter a number ==> '))
        if integer == 0 or integer > 998:
            raise ValueError
    except ValueError:
        print('Enter a valid number (between 1 and 998) !!!')
    else: break

if isPrime(integer) == True:
    print(f'--> The number {integer} is a prime number!')
else:
    print(f'--> The number {integer} is not a prime number!')

