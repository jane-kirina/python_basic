from sympy import *
from sympy.plotting import plot3d
import random

separator_header = '-------------------------'

'''Plot Examples'''
print(separator_header + 'Plot Examples')
print('f(x) = x^2 + 1')
x = symbols('x')
f = x ** 2 + 1
plot(f)

print('f(x) = x^3 - 10')
x = symbols('x')
f = x ** 3 + 10
plot(f)

print('f(x) = x^(1/2)')
x = symbols('x')
f = x ** (1/2)
plot(f)

'''Limits'''
print(separator_header + 'Limits')

x = symbols('x')
f = 1 / x
result = limit(f, x, oo)
print(result)  # 0

'''Limits - Euler's Number'''
print(separator_header + "Limits - Euler's Number")

n = symbols('n')
f = (1 + (1 / n)) ** n
result = limit(f, n, oo)
print(result)
print(result.evalf())

'''Derivatives'''
# for f(x) = x^2 at x=2
print(separator_header + 'Derivatives')
#A derivative tells the slope of a function, and it is useful to measure the rate of change at any point in a function.

def derivative_x(f, x, step_size):
    return (f(x + step_size) - f(x)) / ((x + step_size) - x)


def func(x):
    return x ** 2


slop = derivative_x(func, 2, .1)
print(slop)

'''Derivatives - sympy'''
print(separator_header + 'Derivatives - sympy')

# s - step size
x, s = symbols('x s')
f = x ** 2

# slop between 2 points with step s
slop_f = (f.subs(x, x + s) - f) / ((x + s) - x)

# substitute 2 for x
slop_at_2 = slop_f.subs(x, 2)

# calculate slop at x=2
result = limit(slop_at_2, s, 0)

print(result)

'''Derivatives - sympy dif()'''
print(separator_header + 'Derivatives - sympy dif()')

x = symbols('x')
f = x ** 2
dx_f = diff(f)
print(dx_f)

'''Partial Derivatives'''
print(separator_header + 'Partial Derivatives')

print('graph of a function')
x, y = symbols('x y')
f = 2 * x ** 3 + 3 * y ** 3
dx_f = diff(f, x)
dy_f = diff(f, y)

print(f)
print(f'dx_f = {dx_f}')
print(f'dy_f = {dy_f}')

plot3d(f)

'''Gradient Descent'''
print(separator_header + 'Gradient Descent')


def f(x):
    return (x - 4) ** 2 + 4


def dx_f(x):
    return 2 * (x - 3)


# learning rate, scale how small steps are
L = 0.001
# the number of iterations to perform gradient descent
epochs = 100000

x = random.randint(-15, 15)

for i in range(epochs):
    d_x = dx_f(x)  # slop
    x = x - L * d_x

print(x, f(x))

'''Integrals'''
print(separator_header + 'Integrals')
# The opposite of a derivative is an integral, wich finds an area under a func's curve

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)
    return total_sum * delta_x


area = approximate_integral(a=0, b=2, n=10000, f=func)

print(area)

'''Limits and Reimann Sum'''
print(separator_header + 'Limits and Reimann Sum')

x, i, n = symbols('x i n')

f = x ** 2
lower, upper = 0, 2

# Calculate width and each rectangle height at index
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# Iterate al L "n" rectangles and sum their areas
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# Calculate the area by approaching the number of rectangles "n" to infinity
area = limit(n_rectangles, n, oo)

print(area)

'''Integrals - using sympy'''
print(separator_header + 'Integrals - using sympy')

x = symbols('x')
f = x ** 2

area = integrate(f, (x, 0, 2))
print(area)
