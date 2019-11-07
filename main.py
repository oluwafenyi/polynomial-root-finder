
from bisection import bisection_find_root
from secant import secant_find_root
from newton_raphson import nr_find_root


def get_polynomial():
    n = int(input('The polynomial is of what degree? '))
    coefficients = [eval(input(f'Enter coefficient for x^{n-i}: ')) for i in range(n+1)]
    print()
    return coefficients

def collect_args(method):
    if method == 'nr':
        x = float(input('Enter initial guess x\u2080: '))
        print()
        return x

    elif method == 'bisection':
        a, b = list(map(float, input('Input interval a and b such that a < b in the form "a,b": ').split(',')))
        print()
        return a, b

    elif method == 'secant':
        x0 = float(input('Enter initial guess x\u2080: '))
        x1 = float(input('Enter initial guess x\u2081: '))
        print()
        return x0, x1


if __name__ == '__main__':
    coefficients = get_polynomial()
    epsilon = float(input('Enter desired accuracy: '))
    method = input('Pick method:\n1. Bisection Method.\n2. Secant Method.\n3. Newton-Raphson Method.\n:\n')
    print()
    switch = {
        '1': 'bisection',
        '2': 'secant',
        '3': 'nr',
    }
    method = switch.get(method, None)
    if method == None:
        raise ValueError('Invalid option chosen.')

    args = collect_args(method)

    switch = {
        'bisection': bisection_find_root,
        'secant': secant_find_root,
        'nr': nr_find_root
    }
    function = switch.get(method)
    epsilon = epsilon if epsilon else 0.00001

    if type(args) == float:
        function(coefficients, args, epsilon)
    else:
        function(coefficients, *args, epsilon)
