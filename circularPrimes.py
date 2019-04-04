from PrimeLib import isPrime2
from PrimeLib import generate_prime_list


def rotate(rotatee,rotater):
    LFirst = str(rotatee)[0:rotater]
    LSecond = str(rotatee)[rotater: ]
    rotated = int(LSecond + LFirst)
    return rotated


primes = generate_prime_list(1000000)
for prime in primes:
    splitPrime = list(str(prime))
    for char in range(len(splitPrime)):
        rotated = rotate(prime,char)
        if isPrime2(rotated) == True:
            pass
        else:
            primes.remove(prime)
print(len(primes))
#Breaks at 137 because the program tries to remove it twice