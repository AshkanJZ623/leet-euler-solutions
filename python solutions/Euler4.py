def is_palindromic(n):

    flag = False
    if n > 1:
        a = [int(x) for x in str(n)]
        while len(a) > 0:
            if len(a) == 1:
                return True
            if len(a) > 0:
                if a[0] == a[-1] :
                    a.remove(a[0])
                    a.pop()    
                    flag = True
                else:
                    flag = False
                    break
        return flag

def make_palindromic(n):
    
    a = []
    if n == 2: 
        for i in range (10 , 100):
            for j in range(10, 100):
                k = i*j
                if k not in a:
                    if is_palindromic(k):
                        a.append(k)          
        print(max(a))

    if n == 3: 
        for i in range (100 , 1000):
            for j in range(100 ,1000):
                k = i*j
                if k not in a:
                    if is_palindromic(k):
                        a.append(k)         
        print(max(a))

a = int(input("enter your number of digits: "))
print(make_palindromic(a))

