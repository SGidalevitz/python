#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143?
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

def largest_prime_factor(n):
    list = []
    i = 2
    x = 0
    a = i
    while i < (n / 2):
        if  n % i == 0 and fermat(i):
            x = i
            a = x / i
            i = 2
            list.append(a)
            print(list)  
        i += 1
    return x
print(largest_prime_factor(600851475143))

            
