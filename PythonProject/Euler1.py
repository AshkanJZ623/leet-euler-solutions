def mult_three_five():

    n = int(input("enter your desired number: "))
    sum = 0
    for i in range(1 , n):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    print("sum of the mults of 3 and 5 below", n , "is:", sum)

mult_three_five()
            
