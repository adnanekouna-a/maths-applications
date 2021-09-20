def factorial(num: int) -> int:
    '''Calculates the factorial'''
    if num in [0,1]:
        return 1
    return num*factorial(num-1)

if __name__ == '__main__':
    try:
        number = int(input('Enter the number : '))
        if number < 0:
            raise ValueError
        result = factorial(number)
        print(f'The factorial of {number} is {result}')
    except ValueError:
        print('You have to enter a positive number!!!')
    except RecursionError:
        print('The maximum number you can calculate the factorial for is "998"!')
