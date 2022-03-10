import math

def is_prime(n):
    if n == 2:
        return True
    if n > 2:
        for i in range (2, int(math.sqrt(n)+1)):
            a = n % i
            if a == 0:
                return False
        else:
            return True

def prime_count():

    count = 0
    a = []
    i = 0
    while count < 10001:
        i += 1
        if is_prime(i):
            a.append(i)
            count += 1
    print(a[-1] , count)

prime_count()