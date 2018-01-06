import random

print("##{:#<78}".format(" assignment packing "))
t = (0, 1, 2, 3, 4)
*a, b, c = t
print(a, b, c)              # -> [0, 1, 2] 3 4
a, *b, c = t
print(a, b, c)              # -> 0 [1, 2, 3] 4
a, b, *c = t
print(a, b, c)              # -> 0 1 [2, 3, 4]
_, _, *c = t
print(c)                    # -> [2, 3, 4]
print(t[2:])                # -> [2, 3, 4]
g = (x for x in range(5))   # generator expression
_, _, *c = g
print(c)                    # -> [2, 3, 4]
# print(g[2:])  # TypeError: 'generator' object is not subscriptable

print("##{:#<78}".format(" assignment unpacking "))
a, b = (0, 1)
print(a, b)                     # -> 0 1
((a, b), (c, d)) = ((0, 1), (2, 3))
print(a, b, c, d)               # -> 0 1 2 3
a, b = [*(0, 1)]
print(a, b)                     # -> 0 1
a, b = *(0, 1),
print(a, b)                     # -> 0 1
t0 = (0, 1)
t1 = (2, 3)
a, b, c, d = *t0, *t1
print(a, b, c, d)               # -> 0 1 2 3
a, *b, c = *t0, *t1
print(a, b, c)                  # -> 0 [1, 2] 3
a, b = *(x for x in range(2)),  # generator expression
print(a, b)                     # -> 0 1
d = {"a": 0, "b": 1, "c": 2, "d": 3}
a, b, c, d = *d,                # unpacking dictionary keys
print(a, b, c, d)               # -> unreliably ordered a b c d

print("##{:#<78}".format(" dictionary unpacking "))
x = "a aa b bb c cc".split()
x = list(zip(x[::2], x[1::2]))
d = dict(x)


def f(a, b, c):
    print(a, b, c)


f(**d)  # unpacking
print(x)
print(list(zip(*x)))    # transposed

print("##{:#<78}".format(" original sequence unpacking "))


class IterableContainer:
    def __iter__(self):
        return Iterator()


class Iterator:
    def __next__(self):
        x = random.randrange(100)

        if x >= 90:
            raise StopIteration
        else:
            return x


def f(*args):       # packing
    print(*args)    # unpacking


f(*IterableContainer())

print("##{:#<78}".format(" original dictionary unpacking "))


class Dictionary:
    def keys(self):
        x = []

        for _ in range(3):
            x.append(str(random.randrange(100)))

        return x

    def __getitem__(self, key):
        return 2 * int(key)


def f(**kwargs):    # packing
    print(kwargs)


f(**Dictionary())   # unpacking
