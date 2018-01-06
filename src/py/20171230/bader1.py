import inspect
import unittest


def f_default():
    return inspect.stack()[0][3]


def f0():
    return inspect.stack()[0][3]


def f1():
    return inspect.stack()[0][3]


class Test(unittest.TestCase):
    def test0(self):
        c = "condition0"
        x = {"condition0": f0, "condition1": f1}.get(c, f_default)()
        self.assertEqual("f0", x)

        c = "condition1"
        x = {"condition0": f0, "condition1": f1}.get(c, f_default)()
        self.assertEqual("f1", x)

        c = "condition_x"
        x = {"condition0": f0, "condition1": f1}.get(c, f_default)()
        self.assertEqual("f_default", x)


unittest.main()
