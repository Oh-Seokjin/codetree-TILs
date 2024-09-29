n, m = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
###

for i in range(n):
    w, p = jewels[i][0], jewels[i][1]
    jewels[i].append(p/w)

jewels.sort(key=lambda x: x[2], reverse=True)

bag_value = 0

while True:
    if not jewels:
        break
    if jewels[0][0] <= m:
        bag_value += jewels[0][1]
        m -=jewels[0][0]
        jewels.pop(0)
    else:
        bag_value += jewels[0][2]*m
        break

print(f"{bag_value:.3f}")