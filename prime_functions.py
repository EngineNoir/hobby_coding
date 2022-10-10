import numpy as np


def check_if_prime():

    x = int(input("Please input an integer: "))

    is_prime = True
    upper_bound = int(np.floor(np.sqrt(x))) + 1
    divisor = 1

    if x == 1:
        print("1 is 1 and not a prime, silly!\n")
    elif x == 2:
        print("2 is a prime!\n")
    else:
        for i in range(2, upper_bound):
            if (x % i) == 0:
                is_prime = False
                divisor = i
                break
            else:
                continue

        if is_prime:
            print(str(x) + " is a prime!\n")
        else:
            print(str(x) + " is not a prime, since it is divisible by " + str(divisor) + ".\n")


def check_if_prime2(x, prime_list):
    is_prime = True
    upper_bound = int(np.floor(np.sqrt(x))) + 1

    if x == 1:
        x
    elif x == 2:
        prime_list.append(x)
    else:
        for i in range(2, upper_bound):
            if (x % i) == 0:
                is_prime = False
                break
            else:
                continue

        if is_prime:
            prime_list.append(x)
        else:
            x


def primes_up_to():
    n = int(input("Please input the number for which you want to see all primes below it: "))
    primes = []

    for i in range(1, n):
        check_if_prime2(i, primes)
    print(primes)
    print("There are " + str(len(primes)) + " primes below " + str(n) + ".")
    print("\n")


def prime_functions():
    key = int(input("Type 1 to see if a specific number is prime. \n"
                    "Type 2 to see which numbers are prime up to a chosen number. \n"
                    "Input: "))
    if key == 1:
        check_if_prime()
        prime_functions()
    elif key == 2:
        primes_up_to()
        prime_functions()
    else:
        prime_functions()

    print("\n")


prime_functions()
