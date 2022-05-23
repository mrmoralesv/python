#
# please refer to PPT file
# for exercise
#
# Tarea Tema 4 :Resolver usando uno de los  metodos a elegir y obtener la raiz
# e^(2-x)-7x=0
import matplotlib.pyplot as plp
from math import exp
import numpy as np

# La funcion original


def fn1(x):
    y = exp(2-x) - 7*x
    return y


X = np.arange(-2, 2, 1)
Y = [fn1(i) for i in X]

print("Puntos X:", X)
print("Puntos Y:", Y)

plp.plot(X, Y)
plp.show()

# La funcion derivada


def fn2(x):
    y = -exp(2-x) - 7
    return y


X = np.arange(-1, 5, 1)
Y = [fn2(i) for i in X]

print("Puntos X:", X)
print("Puntos Y:", Y)

plp.plot(X, Y)
plp.show()
