x = list(range(10))
x2 = [2 * x for x in x]
x3 = [2 * x for x in x2]
x = list(zip(x, x2, x3))
print(x)
x = [(*x2, x) for x, *x2 in x]
print(x)
print("=" * 80)

a = ((1, 2), (3, 4), (5, 6))
x0, *x1 = a
print(x0, x1)
print("=" * 80)

a = (0, 1, 2)
b = (3, 4, 5)
c = (6, 7, 8)
d = (9, 10, 11)
d = (a, b, c)
# x = *(1, *a), 2, (3, *b)
x = d
print(x)
print("=" * 80)


[x, y, z] = [0, 1], *[*[*[2]], 3]
print(x, y, z)
[*[x]] = [*[1]]
print(x)
[[[x]]] = [[[1]]]
print(x)
[x] = [*[*[1]]]
[x] = ([(*([(*([(1)]))]))])
print(x)
# [x] = [**[[1]]]
# [x] = [*(*[[1]])]
print(x)
