from math import sqrt

print("Quadratic Equations' Solver")


def quadratic(a, b, c):
    Delta = (b**2) - 4*a*c
    if Delta < 0:
        return "This equation has no solution"
    elif Delta == 0:
        x = -(b/(2*a))
        return f"There's only one solution, which is {x}."
    elif Delta > 0:
        x1 = ((-b) + sqrt(Delta))/(2*a)
        x2 = ((-b) - sqrt(Delta))/(2*a)
        return f"This equation has two solutions, {x1} and {x2}."


try:
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print(quadratic(a, b, c))
except ValueError:
    print('You should enter numerical Values!!!')
except ZeroDivisionError:
    print("a can't equal 0!!!")
