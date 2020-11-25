def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        0
        return n*factorial(n-1)


number = int(input('Enter the number : '))
result = 0

if number == 0:
    result = 1
else:
    result = factorial(number)

print(f'The factorial of {number} is {result}')

# TODO fix negative numbers
