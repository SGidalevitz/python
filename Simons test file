import time
Hamelin = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
def prime(n):
   a = 0
   i = 2
   while i < n:
    for x in range (2,i-1):
        if (i % x) == 0:
            a = 1
    if a == 0: 
        print(i)
    a = 0
    i = i + 1
def primecheck(n):
    i = 2
    for x in range (2, n-1):
        if (i % x) != 0:
            return True
        i = i + 1
    return False
def gen_coprime(n):
    e621 = 0
    i = 2
    while e621 != 1:
        if n % i == 0:
            i = i + 1
        else:
            return i           
def fermat(n):
    
    temp = gen_coprime(n)
    if ((temp ** (n-1)) % n) == 1:
        return True
    else:
        return False

def prime_fact(n):
        pass

print(fermat(150))