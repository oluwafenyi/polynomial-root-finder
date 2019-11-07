
from utils import calc_func, calc_derivative, time_it


@time_it
def nr_find_root(coefficients, x, epsilon=0.00001):
    f = calc_func(coefficients)
    g = calc_derivative(coefficients)
    try:
        h = f(x) / g(x)
    except ZeroDivisionError:
        return '{0:.04f}'.format(x)

    while abs(h) >= epsilon:
        h = f(x) / g(x)
        x -= h

    return '{0:.04f}'.format(x)
