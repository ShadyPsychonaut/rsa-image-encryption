import math

from numpy import mat, mod

n = 713
e = 7
d = 283

org_data = 255

c = pow(org_data, e, mod=n)

# for org_data in range(0, 256):
#     c = math.pow(org_data, e)
#     c = c % n
#     print(c)

p = pow(c, d, mod=n)


def extendedEuclid(a, b):
    if(b == 0):
        return a, 1, 0

    gcd, x1, y1 = extendedEuclid(b, a % b)
    x = y1
    y = x1 - (a//b) * y1

    return gcd, x, y


gcd, x, y = extendedEuclid(3, 3016)
