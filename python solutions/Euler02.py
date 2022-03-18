def even(n):

    if n % 2 == 0:
        return True
    else:
        return False

def fib_even_sum():

    sum = 0
    first_ind = 0
    second_ind = 1
    next_ind = 0
    
    while first_ind < 4000000:
        next_ind = first_ind + second_ind
        first_ind = second_ind
        second_ind = next_ind
        if even(first_ind):
            sum += first_ind
            print(sum)

print(fib_even_sum())
