import itertools, math

def triangle():
    tri_sequence = 0
    for i in itertools.count(1):
        tri_sequence += i
        if divisors(tri_sequence) > 500:
            break
    return tri_sequence

def divisors(n):
    
    count = 0
    for i in range(1 , int (math.sqrt(n)+1)):
        if n % i == 0:
            count += 2
    if pow(math.sqrt(n),2) == n :
        count -= 1
    return count

if __name__ == "__main__":
    print(triangle())