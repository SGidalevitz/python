fnumbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733]

def P(n,k):
    if     

#Define function P(n,k) = 1 if n can be written as the sum of k prime numbers (with repetitions allowed), and P(n,k) = 0 otherwise.

#For example, P(10,2) = 1 because 10 can be written as either 3 + 7 or 5 + 5, but P(11,2) = 0 because no two primes can sum to 11.

#Let S(n) be the sum of all P(i,k) over 1 ≤ i,k ≤ n.

#For example, S(10) = 20, S(100) = 2402, and S(1000) = 248838.

#Let F(k) be the kth Fibonacci number (with F(0) = 0 and F(1) = 1).

#Find the sum of all S(F(k)) over 3 ≤ k ≤ 44
