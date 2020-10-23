def multiply(x, y):
    return x*y


def add(x, y):
    return x+y


def substract(x, y):
    return x-y


def divide(x, y):
    return x/y


print('Basic Calculator!')
x = int(input('x = '))
y = int(input('y = '))
operation = input('Operation [A, S, M, D] : ')

if operation == 'A':
    print(add(x, y))
elif operation == 'S':
    print(substract(x, y))
elif operation == 'M':
    print(multiply(x, y))
elif operation == 'D':
    print(divide(x, y))
