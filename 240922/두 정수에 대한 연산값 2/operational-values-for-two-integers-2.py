def sum_two(a, b):
    _min = min(a, b)+10
    _max = max(a, b)*2
    print(_min, _max)

a, b = map(int, input().split())
sum_two(a, b)