def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

a, b = map(int, input().split())
a_divisor = getMyDivisor(1920)
b_divisor = getMyDivisor(2880)
common_divisor = list(set(a_divisor) & (set(b_divisor)))

common = []
for elem in common_divisor:
    if a<=elem<=b:
        common.append(elem)
if common:
    print(1)
else:
    print(0)