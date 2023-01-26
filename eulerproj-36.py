def palindrome(n):
    print(str(n)[:2])
    if len(str(n)) % 2 == 0:

        if str(n)[:(len(str(n))/2)] == str(n)[(len(str(n))/2)+1::-1]:
            return True
    

palindrome(1551)
