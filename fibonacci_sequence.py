print('Which term do you want?')

n1, n2 = 0, 1
count = 0
sequence = []
try:
    term = int(input())
    if term <= 0:
        raise ValueError
    elif term == 1:
        print(f'The Fibonacci Sequence up to 1 is [0].')
    else:
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
