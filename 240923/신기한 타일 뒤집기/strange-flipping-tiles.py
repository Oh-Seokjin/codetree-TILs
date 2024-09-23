n = int(input())

answer = {"L":0, "R":0}

for _ in range(n):
    cnt, direction = input().split()
    cnt = int(cnt)
    
    if direction == "R":
        if "L" not in answer:
            answer[direction] += cnt
        else:
            if answer["L"] >= cnt:
                answer["L"] = answer["L"] - cnt
                answer["R"] = cnt
            else:
                answer["L"] = 0
                answer["R"] = cnt

    if direction == "L":
        if "R" not in answer:
            answer[direction] += cnt
        else:
            if answer["R"] >= cnt:
                answer["R"] = answer["R"] - cnt
                answer["L"] = cnt
            else:
                answer["R"] = 0
                answer["L"] = cnt

print(answer["L"], answer["R"])