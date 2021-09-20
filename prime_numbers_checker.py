from factorial_calculator import factorial

def is_prime(num: int) -> bool:
    '''Verifies if an integer is prime'''
    if num == 1:
        return False
    if factorial(num-1)%num == (num-1):
        return True
    return False

if __name__ == '__main__':
    while True:
        try:
            integer = int(input('Enter a number ==> '))
            if integer == 0 or integer > 998:
                raise ValueError
            break
        except ValueError:
            print('Enter a valid number (between 1 and 998) !!!')

    if is_prime(integer) == True:
        print(f'--> The number {integer} is a prime number!')
    else:
        print(f'--> The number {integer} is not a prime number!')
