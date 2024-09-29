# cmp_to_key 사용 관련하여 해설 확인함

n = int(input())
arr = [int(input()) for _ in range(n)]
###


def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    if str(a) + str(b) < str(b) + str(a):
        return 1
    return 0

arr.sort(key=cmp_to_key(compare))

for elem in arr:
    print(elem, end="")