def is_pandigital(n: int) -> bool:
    n = str(n)
    if len(n) < 18:
        return False
    first_nine = n[:9]
    last_nine = n[-9:]
    pandigital = "123456789"
    if sorted(first_nine) == list(pandigital) and sorted(last_nine) == list(pandigital):
        return True
    else:
        return False

def fibonacci_pandigital():
    a = 1
    b = 1
    k = 2
    while True:
        c = a + b
        k += 1
        if is_pandigital(c):
            return k
        a = b
        b = c

print(f"k: {fibonacci_pandigital()}")