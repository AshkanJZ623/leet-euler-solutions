def sum_of_squares(n):
    sum = 0
    for i in range (1 , n + 1):
        for j in range (1 , n + 1):
            if i == j:
                k = i * j
        sum += k
    # print(sum)
    return sum

def square_of_sum(n):
    sum = 0
    for i in range (1 , n + 1):
        sum += i
        square_of_sum_nums = sum * sum
    # print(square_of_sum_nums)
    return square_of_sum_nums

def diff(n):
    first = square_of_sum(n)
    second = sum_of_squares(n)
    difference = first - second
    print(difference)

a = int(input("Enter your number:"))
diff(a)