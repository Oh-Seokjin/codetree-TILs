def fourth_year(n):
    if n%400 == 0:
        return True
    elif n%100 != 0 and n%4==0:
        return True
    else:
        return False

def is_valid_date(y, m, d):
    if m == 2:
        if fourth_year(y) and d<=29:
            return True
        elif not fourth_year(y) and d<=28:
            return True
    elif m in [4, 6, 9, 11]:
        if d<=30:
            return True
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if d<= 31:
            return True
    else:
        return False

Y, M, D = map(int, input().split())

spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
winter = [12, 1, 2]

if is_valid_date(Y, M, D):
    if M in spring:
        print('Spring')
    elif M in summer:
        print('Summer')
    elif M in fall:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)