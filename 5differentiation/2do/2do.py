#
# please refer to PPT file
# for exercise
#
# Tarea Derivacion numerica
# Resuelve la siguiente derivada con al menos 3 metodos
# Si f(x) = (sen^3)(2x)/x^4+1 obtener f'(2.45) Respuesta =0.0698503
# Diferencias finitas centradas

from math import sin, exp


def fn(x):
    return (pow(sin(2*x), 3)) / (pow(x, 4) + 1)


x0 = 2.45
h1 = 0.1
h2 = 0.00001
h3 = 0.00000001

print("\n Diferencias finitas centradas")

r3 = (fn(x0+h1)-fn(x0-h1))/(2*h1)
print(r3)

r4 = (fn(x0+h2)-fn(x0-h2))/(2*h2)
print(r4)

r5 = (fn(x0+h3)-fn(x0-h3))/(2*h3)
print(r5)

print("\n Diferencias finitas progresivas")

r3 = (fn(x0+h1)-fn(x0))/h1
print(r3)

r4 = (fn(x0+h2)-fn(x0))/h2
print(r4)

r5 = (fn(x0+h3)-fn(x0))/h3
print(r5)

print("\n Derivada de primer orden")

r3 = (fn(x0+h1/2)-fn(x0-h1/2))/h1
print(r3)

r4 = (fn(x0+h2/2)-fn(x0-h2/2))/h2
print(r4)

r5 = (fn(x0+h3/2)-fn(x0-h3/2))/h3
print(r5)
