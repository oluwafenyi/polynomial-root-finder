from utils import calc_func, time_it


@time_it
def bisection_find_root(coefficients, a, b, epsilon=0.00001):
    f = calc_func(coefficients)

    if (f(a) * f(b) >= 0):
        print('Assume a and b such that f(a)f(b) < 0')
        return

    c = (a + b) / 2
    f_c = f(c)

    if f_c == 0:
        return '{0:.04f}'.format(c)

    while b - a > epsilon:
        if f_c * f(a) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        f_c = f(c)
    return '{0:.04f}'.format(c)
