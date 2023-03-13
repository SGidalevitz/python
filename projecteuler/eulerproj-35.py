def checkprime(number):
    for i in range(2, int(number / 2)):
        if number % i == 0:
            return False
    return True
allcirculars = []
for i in range(1, 1000000):
    circulars = []
    if len(str(i)) >= 1:
        index1 = (str(i)[0])
    if len(str(i)) >= 2:
        index2 = (str(i)[1])
    if len(str(i)) >= 3:
        index3 = (str(i)[2])
    if len(str(i)) >= 4:
        index4 = (str(i)[3])
    if len(str(i)) >= 5:
        index5 = (str(i)[4])
    if len(str(i)) >= 6:
        index6 = (str(i)[5])
    if len(str(i)) == 1:
        circulars.append(int(index1))   
    elif len(str(i)) == 2:
        for i in range(2):
            placehold = index1
            index1 = index2
            index2 = placehold
            circulars.append(int(index1 + index2))
    elif len(str(i)) == 3:
        for i in range(3):
            placehold = index1
            index1 = index2
            index2 = index3
            index3 = placehold
            circulars.append(int(index1 + index2 + index3))
    elif len(str(i)) == 4:
        for i in range(4):
            placehold = index1
            index1 = index2
            index2 = index3
            index3 = index4
            index4 = placehold
            circulars.append(int(index1 + index2 + index3 + index4))
    elif len(str(i)) == 5:
        for i in range(5):
            placehold = index1
            index1 = index2
            index2 = index3
            index3 = index4
            index4 = index5
            index5 = placehold
            circulars.append(int(index1 + index2 + index3 + index4 + index5))
    elif len(str(i)) == 6:
        for i in range(6):
            placehold = index1
            index1 = index2
            index2 = index3
            index3 = index4
            index4 = index5
            index5 = index6
            index6 = placehold
            circulars.append(int(index1 + index2 + index3 + index4 + index5 + index6))
    prime = True
    for j in circulars:
        if not checkprime(j):
            prime = False
    if prime:
        allcirculars.append(i)
    print(i)
