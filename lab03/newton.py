

def calculate_zero(f, df, x, stop_condition):
    """
    Newton's method

    :param f: function, takes one argument
    :param df: function, f derivative
    :param x: first zero approximation
    :param stop_condition: function
    :return: tuple (iterations, x, value)
    """
    value, iterations = f(x), 0

    while True:
        iterations += 1
        next_x = x - value/df(x)
        value = f(next_x)

        if stop_condition(f, x, next_x):
            break

        x = next_x

    return iterations, x, value


def interval_zeros(start, end, f, df, stop_condition, step=0.1):
    a, b = start, end

    while a <= b:
        yield (a,) + calculate_zero(f, df, a, stop_condition)
        yield (b,) + calculate_zero(f, df, b, stop_condition)

        a += step
        b -= step
