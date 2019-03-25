from PrimeLib import isPrime2
def primeSummator(n):
    total = 0
    for i in range(2,n):
        if isPrime2(i):
            total += i
    return total


sum = primeSummator(2000000)
print(sum)