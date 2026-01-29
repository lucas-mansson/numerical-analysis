# Given the fixed-point problem: Find x such that x = cos^2(x) + 5.
# Which approximation does the fixed-point iteration generate after 110 iterations with starting
# value 5.5? Write down the obtained approximation with 4 places after the decimal dot (you may
# use commercial rounding on the last digit if necessary)

import math


def g(x): 
    return (math.cos(x))**2 + 5

if __name__ == "__main__":
    x = 5.5 # x0 initial guess

    for _ in range(110):
        x = g(x)

    print(x)
