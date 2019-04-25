from PrimeLib import isPrime2
from PrimeLib import generate_prime_list
import numpy as np

# np.roll

def rotate(rotatee,rotater):
    LFirst = str(rotatee)[0:rotater]
    LSecond = str(rotatee)[rotater: ]
    rotated = int(LSecond + LFirst)
    return rotated


primes = []
for i in range(1000000):
    primes.append(i)
for prime in primes:
    if isPrime2(prime) == False:
        primes.remove(prime)
for prime in primes:
    splitPrime = list(str(prime))
    for char in range(len(splitPrime)):
        rotated = rotate(prime,char)
        if isPrime2(rotated) == True:
            pass
        else:
            if prime in primes:
                primes.remove(prime)
print(len(primes))
#Breaks at 137 because the program tries to remove it twice