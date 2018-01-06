import sys  # F401 'sys' imported but unused
import subprocess

# E501 line too long (80 > 79 characters)
"123456789012345678901234567890123456789012345678901234567890123456789012345678"


def f():
    x = 0  # F841 local variable 'x' is assigned to but never used


try:
    subprocess.check_output(
        "flake8 flake8.py", stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    output = e.output.decode("utf-8")
    print(output, end="")

# W391 blank line at end of file

