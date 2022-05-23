#
# radious of circle inscribed in a triangle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

from cmath import sqrt


a = 3
b = 4
c = 6

s = 0.5*(a + b + c)

r = (sqrt(s*(s - a)*(s - b)*(s - c))) / s


print(r)
