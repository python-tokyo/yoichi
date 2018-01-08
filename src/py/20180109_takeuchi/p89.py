import pprint


def functions():
    s = """
    f0  eee eee
    f1  --e -r2
    f2  -r3 -r9
    f3  wl4 -r3
    f4  -l5 -l4
    f5  -l5 -l6
    f6  -r2 -r7
    f7  -r8 er7
    f8  -r8 -r3
    f9  wr9 -l10
    f10 --e er11
    f11 w-e -r11
    """
    x = s.strip().splitlines()
    x = [x.split() for x in x]
    pprint.pprint(x)
    return x


class Tape:
    _d = {}

    def __getitem__(self, key):
        return self._d.get(key, 0)

    def __setitem__(self, key, value):
        self._d[key] = value

    def s(self, from_, to):
        s = ""
        for i in range(from_, to + 1):
            s += str(self[i])
        return s


class Machine:
    def __init__(self, tape, location, functions):
        self._t = tape
        self._i = location
        self._fs = functions
        self._f = 1
        self._time = 0

    def _print(self):
        s_time = self._time
        s_func = "fn{}".format(self._f)
        s_tape = self._t.s(0, 6)
        print("{: >2} {: <4} {} at {}".format(s_time, s_func, s_tape, self._i))

    def do(self):
        f = self._fs[self._f]
        t = self._t[self._i]

        if t == 0:
            f = f[1]
        elif t == 1:
            f = f[2]
        else:
            raise Exception

        self._print()
        self._time += 1
        w, lr, next = f[0], f[1], f[2:]

        if w == "w":
            self._t[self._i] = 1
        elif w == "e":
            self._t[self._i] = 0
        elif w == "-":
            pass
        else:
            raise Exception

        if lr == "l":
            self._i += -1
        elif lr == "r":
            self._i += +1
        elif lr == "-":
            pass
        else:
            raise Exception

        if next == "e":
            self._print()
            return
        else:
            self._f = int(next)
            self.do()


if __name__ == "__main__":
    t = Tape()
    t[1], t[2] = [1] * 2
    m = Machine(t, 2, functions())
    m.do()
