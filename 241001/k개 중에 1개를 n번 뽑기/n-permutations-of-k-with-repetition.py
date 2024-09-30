k, n = map(int, input().split())
###

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr, n-1):
            result.append([elem] + rest)
    return result

arr = [elem for elem in range(1, k+1)]

result = combination(arr, n)

for row in result:
    for elem in row:
        print(elem, end=" ") 
    print()