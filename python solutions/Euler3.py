def is_prime(n):

    flag = False
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
        return flag

def prime_factors_finder(n):
    prime_factors = []
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                if is_prime(i):
                    break
                prime_factors.append(i)
        print("Prime factors list:" , prime_factors)
        print("Largest prime factor is:" , max(prime_factors)) 

a = int(input("enter your desired number: "))
print(prime_factors_finder(a))

