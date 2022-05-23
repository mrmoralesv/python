#
# generate a function to produce points
# to be used as x-axis
#
# INPUT
# -> a initial point
# -> b final point
# -> c increment
#
# OUTPUT
# <- list of points
#
# for instance for this range [1,10,.1]
# it will produce 100 points
# [1.0, 1.1, ... , 9.9, 10]
import matplotlib.pyplot as plp
import numpy as np

X = np.arange(0, 10, .10)
Y = (X*2 + 1000)

print("Puntos X:", X)
print("Puntos Y:", Y)

plp.plot(X, Y)
plp.show()
