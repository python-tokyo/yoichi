import random


def r():
    return random.randrange(10)


def get20():
    return [r() for _ in range(20)]


def to_s(x):
    x = [str(x) for x in x]
    x = "".join(x)
    return x


if __name__ == "__main__":
    random.seed(0)
    x = [get20() for _ in range(2)]
    x = [to_s(x) for x in x]
    for x1 in x:
        print(x1)
    print()
    x = [int(x) for x in x]
    for i in range(10):
        print(i, "{:,}".format(x[0] * i))
    acc = 1
    for x in x:
        acc *= x
    print("{:,}".format(acc))
