a = int(input())
for elem in range(1, a+1):
    quotient_8 = elem//8
    remainder_7 = elem%7
    if (elem%2==0 and elem%4!=0) or (quotient_8%2==0) or (remainder_7 < 4):
        continue
    else:
        print(elem, end=" ")