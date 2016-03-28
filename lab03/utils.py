
def get_first_stop_condition(rho):
    def stop_condition(func, x, next_x):
        return abs(next_x - x) < rho
    return stop_condition


def get_second_stop_condition(rho):
    def stop_condition(func, x, next_x):
        return abs(func(x)) < rho
    return stop_condition
