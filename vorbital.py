import math

def vorbital(G=   6.67428e-11, M= 5.9742e24, r = 0.01*149.6e6 * 1000):
    return math.sqrt(G*M/r)


print(vorbital())