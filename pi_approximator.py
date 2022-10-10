import numpy as np
import random
import math


def ratio_approximation(n):
    #note that pi = points with d(x, 0) <= 1, in xdomain = [0, 1) and ydomain = [0, 1)

    X = np.random.rand(n, 2)  #generate n points, the more points the better approximation
    i = 0  #amount of points d(x,0) <= 1
    for coordinate in X:
        if np.sqrt(np.power(coordinate[0], 2) + np.power(coordinate[1], 2)) <= 1:
            i += 1
    return 4*(i/n)


def approximation_mountain():
    print(ratio_approximation(10))
    print(ratio_approximation(100))
    print(ratio_approximation(1000))
    print(ratio_approximation(10000))
    print(ratio_approximation(100000))
    print(ratio_approximation(1000000))

#approximation_mountain()

def approximation_averages(m):
    i = 0
    sum = 0
    while i < m:
        sum += ratio_approximation(100000)
        i += 1
    average = sum/m
    print(average)

#approximation_averages()

def series_pi(n):
    i = 1
    sum = 0
    while i < n:
        sum += (1 / i**2)
        i += 1
    print(math.sqrt(6*sum))


#series_pi(100000)

def painful_pi(n):
    i = 0
    sum = 0
    while i < n:
        numerator = math.factorial(4*i)*(1103 + 26390*i)
        denominator = (math.factorial(i)**4)*(396**(4*i))
        sum += numerator/denominator
        i += 1
    constant = (2*math.sqrt(2))/9801
    pie = 1/(constant*sum)
    print(pie)


#painful_pi(5)

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


def probability_pi(n):
    i = 0
    outcomes = 0
    while i < n:
        x = np.random.randint(0, 100)
        y = np.random.randint(0, 100)
        if is_coprime(x, y):
            outcomes += 1
        i += 1
    P = outcomes/n
    pie2 = math.sqrt(6/P)
    print(pie2)


probability_pi(100000)
print(math.pi)
