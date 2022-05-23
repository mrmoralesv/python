# Tarea 1 dados (-4,-2) y (1,5) estimar el valor para x cuando y = 3.7
p1 = (-4, -2)
p2 = (1, 5)

y = 3.7


def fn(p1, p2):
    x = ((p2[0] - p1[0]) / (p2[1] - p1[1])) * (y - p1[1]) + p1[0]
    return x


print(fn(p1, p2))
print(1/14)
