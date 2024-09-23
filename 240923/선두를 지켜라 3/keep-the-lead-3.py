n, m  = map(int, input().split())

total_time = 0
a_pos = 0
b_pos = 0
a_moves = []
b_moves = []
hall_of_fame = ["C"]

for _ in range(n):
    a_move = tuple(map(int, input().split()))
    total_time += a_move[1]
    for i in range(a_move[1]):
        a_moves.append(a_move[0])
for _ in range(m):
    b_move = tuple(map(int, input().split()))
    for i in range(b_move[1]):
        b_moves.append(b_move[0])

for i in range(total_time):
    a_pos += a_moves[i]
    b_pos += b_moves[i]
    if a_pos > b_pos and hall_of_fame[-1] != "A":
        hall_of_fame.append("A")
    elif a_pos < b_pos and hall_of_fame[-1] != "B":
        hall_of_fame.append("B")
    elif a_pos == b_pos and hall_of_fame[-1] != "AB":
        hall_of_fame.append("AB")

hall_of_fame.remove("C")
print(len(hall_of_fame))