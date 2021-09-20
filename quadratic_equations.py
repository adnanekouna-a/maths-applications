from math import sqrt

print("Quadratic Equations' Solver")

def quadratic(a_fact, b_fact, c_fact):
    '''Solves quadratic equations'''
    delta = (b_fact**2) - 4*a_fact*c_fact
    if delta < 0:
        return "This equation has no solution."
    if delta == 0:
        x = -(b_fact/(2*a_fact))
        return f"There's only one solution, which is {x}."
    x1 = ((-b_fact) + sqrt(delta))/(2*a_fact)
    x2 = ((-b_fact) - sqrt(delta))/(2*a_fact)
    return f"This equation has two solutions, {x1} and {x2}."

if __name__ == '__main__':
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
    except ValueError:
        print('You should enter numerical Values!!!')
    except ZeroDivisionError:
        print("a can't equal 0!!!")
    print(quadratic(a, b, c))
