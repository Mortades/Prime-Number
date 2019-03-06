import time
time.time()

def prime_check_v1(x):
    check = 1
    if x == 2 and x == 3:
        check = 1
    elif x == 1:
        check = 0
    else:
        for i in range(2, x - 1):# think carefully on this line
            # Explain a little bit more here........
            check *= x % i# Do we need this line?
    if check == 0:
        answer = 0
    else:
        answer = 1
    return answer
# 0.031998634338378906

def prime_check_v2(x):
    check = 1 #Tempted to amke check answer to save one if statement but would result in fully running for loop in some cases
    x = int(x)
    if x < 2: #0,1 not primes and negative numbers not included in what our program was supposed to do
        answer = 0
    elif x == 2 and x == 3: #2 and 3 need exceptions in our program
        answer = 1
    elif x % 2 == 0: #Even numbers not prime so unnecessary to use for loop and waste processing power
        answer = 0
    else:
        for i in range(2, x - 1):
            check *= x % i
            if check == 0:
                answer = 0
            else:
                answer = 1
    return answer


def prime_check_v3(x):
    check = 1
    x = int(x)
    if x < 2: #0,1 not primes and negative numbers not included in what our program was supposed to do
        answer = 0
    elif x == 2 and x == 3: #2 and 3 need exceptions in our program
        answer = 1
    else:
        for i in range(2, int(x ** 0.5)):
            check *= x % i
            if check == 0:
                answer = 0
            else:
                answer = 1
    return answer



# Run v1 and see run time
tStart = time.time()
for i in range(1000):
    prime_check_v1(97)
tEnd = time.time()
print('Run time v1 = ',tEnd - tStart)

tStart = time.time()
for i in range(1000):
    prime_check_v2(97)
tEnd = time.time()
print('Run time v2 = ',tEnd - tStart)

tStart = time.time()
for i in range(1000):
    prime_check_v3(97)
tEnd = time.time()
print('Run time v3 = ',tEnd - tStart)

#Run prime number chekc v2 and check run time




# prime_check(1)
# prime_check(2)
# prime_check(20)
# Comment is only for human not for python