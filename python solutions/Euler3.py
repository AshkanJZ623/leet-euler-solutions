import math
import time



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

def prime_factors_finder(n):

    prime_factors = []
    if n > 1:
        if is_prime(n):
            prime_factors.append(n)
            print("Your number" , n, "is prime") 
        else:
            for i in range(2,int(math.sqrt(n)+1)):
                if (n % i) == 0:
                    if is_prime(i):
                        prime_factors.append(i)
                        # n //= i
            print("Prime factors list:" , prime_factors)
            print("Largest prime factor is:" , max(prime_factors))  
        
# start_time = time.time()


a = int(input("enter your desired number: "))
print(prime_factors_finder(a))

# print(time.time() - start_time, "seconds")
