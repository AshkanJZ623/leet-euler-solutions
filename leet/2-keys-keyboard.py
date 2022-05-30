factors = []

def prime(n):

    if n == 2 or n == 3:
        return n
    elif n > 3: 
        for j in range(2, n):
            if n % j == 0 :
                break
        else:
            return n

def leet(i):

    if prime(i):
        factors.append(i)

    else:
        current = 2
        while i > 1:

            if (i % current == 0):
               factors.append(current)
               i = i / current
            else:
                current += 1 

n = int(input("enter you number: "))
leet(n)
print (factors)
print("number of needed operations are: ", sum(factors))