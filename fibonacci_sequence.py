print('Up to which term do you want?')
try:
    term = int(input('> '))
    if term <= 0:
        raise ValueError
    if term == 1:
        print('The Fibonacci Sequence up to 1 is [0].')
    else:
        count = 0
        n1, n2 = 0, 1
        sequence = []
        while count < term:
            sequence.append(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
        print(
            f'The Fibonacci Sequence up to the {term}th term is : {sequence}.')
except ValueError:
    print('Enter a positive number!')
