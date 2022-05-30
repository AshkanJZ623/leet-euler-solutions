

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

def sum_prime_below(n):

	sum = 0
	for i in range(n,1,-1):
		if is_prime(i):
			sum += i
	print(sum)


a = int(input("Enter your number: "))
print(sum_prime_below(a))










# def Pythagorean_triplet(a,b,c):
# 	if a < b < c:
# 		if pow(a,2) + pow(b,2) == pow(c,2):
# 			return a,b,c

# def mult(a,b,c):
# 	d = a*b*c
# 	return d

# def make_pythagorean(my_range):
# 	for i in range(1, my_range):
# 		for j in range(i + 1,my_range):
# 			c = my_range - i - j
# 			if Pythagorean_triplet(i,j,c):
# 				res = mult(i,j,c)
# 				return Pythagorean_triplet(i,j,c) , "multiplication of these numbers is:" , res

# pythatill = int(input("Enter your range: "))
# print(make_pythagorean(pythatill))

