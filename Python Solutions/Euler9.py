
def Pythagorean_triplet(a,b,c):
	if a < b < c:
		if pow(a,2) + pow(b,2) == pow(c,2):
			return a,b,c

def mult(a,b,c):
	d = a*b*c
	return d

def make_pythagorean(my_range):
	for i in range(1, my_range):
		for j in range(i + 1,my_range):
			c = my_range - i - j
			if Pythagorean_triplet(i,j,c):
				res = mult(i,j,c)
				print(Pythagorean_triplet(i,j,c) , "multiplication of these numbers is:" , res)
				

pythatill = int(input("Enter your range: "))
print(make_pythagorean(pythatill))

