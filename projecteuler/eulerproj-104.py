fibonacci = [1,1]

def pcbeg(n):
    check = []
    through19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(str(n)) > 10:
        for x in range(1,11):
            check.append(int(str(n)[x-1]))
        checks = all(item in check for item in through19)
    
        if checks is True:   
            check = []
            through19 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x in range(1,11):
                check.append(int(str(n)[-x]))
            checks = all(item in check for item in through19)
        
            if checks is True:
                return True    
            else :
                return False
        else:
            return False


def run_test():
    global fibonacci
    i = 0
    a = 50
    while i == 0:
        fibonacci.append(fibonacci[0] + fibonacci[1])
        c = fibonacci[2]
        fibonacci.pop(0)
        if a > 329467:
            if pcbeg(c):
                i = 1
        a += 1
        if a % 100 == 0:
            print(a)
    print(c)

run_test()
