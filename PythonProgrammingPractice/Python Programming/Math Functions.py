import math
import sys


def calculate(x, y, z):
    print(min(x, y, z))
    print(max(x, y, z))
    print(math.sqrt(x))
    print(math.ceil(y))
    print(math.floor(y))


calculate(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))