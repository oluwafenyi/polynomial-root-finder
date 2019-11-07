from utils import calc_func, time_it


@time_it
def secant_find_root(coefficients, x0, x1, epsilon=0.00001):
    f = calc_func(coefficients)
    if f(x0) * f(x1) < 0:
        print('Choose x\u2080 and x\u2081 such that f(x\u2080)*f(x\u2081) >= 0')
    h = (f(x1)*(x1 - x0)) / (f(x1) - f(x0))

    while abs(h) >= epsilon:
        h = (f(x1)*(x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 -= h

    return '{0:.04f}'.format(x1)
