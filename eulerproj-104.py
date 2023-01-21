fibonacci = [1,1]

def gen_fibonacci():
    global fibonacci
    fibonacci.append(fibonacci[0] + fibonacci[1])
    return fibonacci[1]
def pcbeg(n):
    check = []
    through19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(str(n)) > 10:
        for x in range(1,11):
            check.append(int(str(n)[x-1]))
        checks = all(item in check for item in through19)
    
        if checks is True:
            return True    
        else :
            return False
    

def pcend(n):
    check = []
    through19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(str(n)) > 10:
        for x in range(1,11):
            check.append(int(str(n)[-x]))
        checks = all(item in check for item in through19)
    
        if checks is True:
            return True    
        else :
            return False

fib = 0
def run_test():
    global fib
    i = 0
    a = 50
    while i == 0:
        c = gen_fibonacci() 
        if pcbeg(c) and pcend(c):
            i = 1
        a += 1
        if a % 1000000 == 0:
            print(a)
            print(c)
            print(fibonacci)
    print(gen_fibonacci(a-1))

run_test()