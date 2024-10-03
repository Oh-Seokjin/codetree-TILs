board = [list(map(int, input().split())) for _ in range(4)]
d = input()
n = 4
###

def gravity():
    global board

    board = [x[::-1] for x in board]

    after = [[]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 마지막은 남아있으면 append
            if j == n-1:
                if board[i][j] > 0:
                    after[i].append(board[i][j])
                continue

            # 0부터 n-1까지
            t1, t2 = board[i][j], board[i][j+1]
            
            # 같으면 두개 합한 후 두개 제거
            if t1 == t2:
                if t1+t2 > 0:
                    after[i].append(t1*2)
                    board[i][j] = 0
                    board[i][j+1] = 0
            # 다르면 해당 칸만 append 
            else:
                if t1 > 0:
                    after[i].append(t1)
                    board[i][j] = 0
        for j in range(n-len(after[i])):
            after[i].append(0)

    after = [x[::-1] for x in after]
    board = after


def rotate(n):
    global board
    if n == 90:
        board = list(map(list, zip(*board[::-1])))
    elif n == 180:
        board = [x[::-1] for x in board[::-1]]
    elif n == 270:
        board = [x[::-1] for x in list(map(list, zip(*board[::-1])))][::-1]

    
if d == "R":
    gravity()
elif d == "L":
    rotate(180)
    gravity()
    rotate(180)
elif d == "U":
    rotate(90)
    gravity()
    rotate(270)
elif d == "L":
    rotate(270)
    gravity()
    rotate(90)

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()