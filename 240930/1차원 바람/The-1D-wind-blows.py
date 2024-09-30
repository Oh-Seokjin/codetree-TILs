n, m, q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]
winds = [list(input().split()) for _ in range(q)]
for i in range(q):
    winds[i][0] = int(winds[i][0])
    if winds[i][1] == "L":
        winds[i][1] = 0
    elif winds[i][1] == "R":
        winds[i][1] = 1
###

def wind(f, direction):
    global building

    # 왼쪽에서 부는 바람
    if direction % 2 == 0:
        temp = building[f-1][m-1]
        building[f-1] = [temp] + building[f-1][:m-1] 
    # 오른쪽에서 부는 바람
    elif direction % 2 == 1:
        temp = building[f-1][0]
        building[f-1] = building[f-1][1:] + [temp]

def up_propagate(f):
    flag = 0
    if f == 0:
        return flag
    c_floor, u_floor = building[f-1], building[f-2]
    for c, u in zip(c_floor, u_floor):
        if c == u:
            flag = 1
    return flag

def down_propagate(f):
    flag = 0
    if f == n:
        return flag
    c_floor, d_floor = building[f-1], building[f]
    for c, d in zip(c_floor, d_floor):
        if c == d:
            flag = 1
    return flag
        

for floor, direction in winds:
    wind(floor, direction)
    up_floor, down_floor = floor, floor
    up_direction, down_direction = direction, direction
    
    while True:
        if up_propagate(up_floor):
            up_floor -= 1
            up_direction += 1
            if up_floor >= 0:
                wind(up_floor, up_direction)
            else:
                break
        else:
            break
    while True:
        if down_propagate(down_floor):
            down_floor += 1
            down_direction += 1
            if down_floor <= n:
                wind(down_floor, down_direction)
            else:
                break
        else:
            break
    
for row in building:
    for elem in row:
        print(elem, end=" ")
    print()