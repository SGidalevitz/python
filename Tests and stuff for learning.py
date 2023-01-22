def prime_factorization(n):
    global factors
    factors = {}
    i = 2
    
    while i * i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n = n // i
        i += 1
    if n > 1:
        factors[n] = 1 
    return factors


def factorss(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result
final = 1
prime_factorization(150)
factorsl = list(prime_factorization(150).values())

print(factorsl)

print(type(factors.get(2)))
print(type(factorsl))
gaming = []
for x in factorsl:
  gaming.append(int(factors.get(x)) + 1)

  
print("gaming")

def combine(n):
  pf = prime_factorization(n)
  pfc = []
  
  for i in pf:
    pfc.append((int(pf.get(pf[i])))+1)
  for i in pfc:
    final = pfc[i] * final
  return final