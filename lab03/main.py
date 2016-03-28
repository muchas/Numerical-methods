import newton
import secant
import plotly.plotly as py
import plotly.graph_objs as go


from utils import get_first_stop_condition


def func_a(x):
    return x**3 + x


def dfunc_a(x):
    return 3*x**2 + 1


condition = get_first_stop_condition(0.001)

for start, iterations, x, value in newton.interval_zeros(-1.5, 1.5, func_a, dfunc_a, condition):
    print("{x},{y},{z}".format(start, x=iterations, y=x, z=value))

print("Secant method")

for start, end, iterations, x, value in secant.interval_zeros(-1.5, 1.5, func_a, condition):
    print("{x},{y},{z}".format(x=iterations, y=x, z=value))
