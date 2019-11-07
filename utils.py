import timeit


def time_it(func):

    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        root = func(*args, **kwargs)
        if root is None:
            return wrapper
        print('The root is: ' + root)
        end = timeit.default_timer()
        print('Function took {0}s to run.'.format(end - start))
    return wrapper


def calc_func(coefficients):
    def wrapper(x):
        degree = len(coefficients) - 1
        total = 0
        for index, coefficient in enumerate(coefficients):
            addend = coefficient * (x**(degree - index))
            total += addend
        return total
    return wrapper


def calc_derivative(coefficients):
    coefficients = coefficients[:-1]
    def wrapper(x):
        degree = len(coefficients)
        total = 0
        for index, coefficient in enumerate(coefficients):
            addend = (degree - index) * coefficient * (x**(degree - index - 1))
            total += addend
        return total
    return wrapper
