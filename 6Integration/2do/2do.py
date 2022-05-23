#
# please refer to PPT file
# for exercise

from math import sin, sqrt


def fn(x):
    return 2 * sin(sqrt(x)) - x


a = 0
b = 1.9724

r1 = fn(a) * (b - a)

print('Regla del Rectángulo I=', r1)

r2 = fn((a + b) / 2) * (b - a)

print('Regla del punto medio I=', r2)

r3 = ((b-a) / 2) * (fn(a) + fn(b))

print('Regla del Trapecio I=', r3)

r4 = ((b - a) / 6) * (fn(a) + 4*fn((a + b) / 2) + fn(b))

print('Regla de Simpson I=', r4)
