n = int(input())

answer = {"L":0, "R":0}
prev_direction = 0

for i in range(n):
    cnt, direction = input().split()
    cnt = int(cnt)

    if i == 0:
        if direction == "L":
            prev_direction = 0
            answer["L"] += cnt
            continue
        if direction == "R":
            prev_direction = 1
            answer["R"] += cnt
            continue

    if direction == "R":
        if prev_direction == 1:
            cnt -= 1
        answer["R"] = answer["R"] + cnt
        answer["L"] = max(answer["L"] - cnt, 0)
        prev_direction = 1

    if direction == "L":
        if prev_direction == 0:
            cnt -= 1
        answer["L"] = answer["L"] + cnt
        answer["R"] = max(answer["R"] - cnt, 0)
        prev_direction = 0
    # print(answer)

print(answer["L"], answer["R"])