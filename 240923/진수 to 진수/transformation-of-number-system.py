def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

a, b = map(int, input().split())
n = input()

print(solution(int(n, a), b))