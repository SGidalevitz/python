import math as m
perimeters = []
from collections import Counter

for p in range(500):
    for i in range(p, 500):
        if int(m.sqrt(i*i + p*p)) == m.sqrt(i*i + p*p):
            perimeters.append(p + i + m.sqrt(i*i + p*p))

p = Counter(perimeters)
print(p.most_common(1)[0])
