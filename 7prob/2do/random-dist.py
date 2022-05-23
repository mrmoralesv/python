#
# select a distribution from random
# produce random numbers on such a distribution
#
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#
import numpy as np

print(np.random.random_integers(5))
# 4
print(type(np.random.random_integers(5)))
# <type 'int' >
print(np.random.random_integers(5, size=(3, 2)))
# array([[5, 4],
#      [3, 3],
#     [4, 5]])
