def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        0
        return n*factorial(n-1)


try:
    number = int(input('Enter the number : '))
    result = 0

    if number == 0:
        result = 1
    elif number < 0:
        raise ValueError
    else:
        result = factorial(number)

    print(f'The factorial of {number} is {result}')
except ValueError:
    print('You have to enter a positive number!!!')
