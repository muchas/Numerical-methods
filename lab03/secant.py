

def calculate_zero(f, a, b, stop_condition):
    """
    Secant method

    :param f: function, takes one argument
    :param a: first zero approximation
    :param b: first approximation
    :param stop_condition: function
    :return: tuple (iterations, x, value)
    """
    val_a, val_b, iterations = f(a), f(b), 0

    while True:
        iterations += 1

        if abs(val_a) > abs(val_b):
            a, b = b, a
            val_a, val_b = val_b, val_a

        s = (b - a)/(val_b - val_a)
        b = a
        val_b = val_a
        a = a - val_a * s
        val_a = f(a)

        if stop_condition(f, b, a):
            break

    return iterations, a, val_a


def interval_zeros(start, end, f, stop_condition, step=0.1):
    a, b = start, end

    while a <= b:
        yield (a, end) + calculate_zero(f, a, end, stop_condition)
        yield (start, b) + calculate_zero(f, start, b, stop_condition)

        a += step
        b -= step
