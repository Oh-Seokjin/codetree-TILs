a, b, x, y = map(int, input().split())

s, e = min(a, b), max(a, b)
t_s, t_e = min(x, y), max(x, y)

t_walk_time = abs(s-t_s) + abs(e-t_e)
walk_time = e-s
print(min(walk_time, t_walk_time)