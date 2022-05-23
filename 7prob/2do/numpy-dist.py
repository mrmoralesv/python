#
# select a distribution from numpy
# produce random numbers on such a distribution
#
# zeeAlso
# e n.wikipedia.org/wiki/Probability_distribution
#
import numpy as np
n, p = 10, .5
s = np.random.binomial(n, p, 1000)
print(s)
