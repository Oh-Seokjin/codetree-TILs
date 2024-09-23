n = int(input())

answer = {"L":0, "R":0}

for _ in range(n):
    cnt, direction = input().split()
    cnt = int(cnt)
    
    if direction == "R":
        if "L" not in answer:
            answer[direction] += cnt
        else:
            if answer["L"] > cnt:
                answer["R"] = answer["R"] + cnt
                answer["L"] = answer["L"] - cnt                
            else:
                answer["R"] = answer["R"] + cnt
                answer["L"] = 0                

    if direction == "L":
        if "R" not in answer:
            answer[direction] += cnt
        else:
            if answer["R"] > cnt:
                answer["L"] = answer["L"] + cnt
                answer["R"] = answer["R"] - cnt
            else:
                answer["L"] = answer["L"] + cnt
                answer["R"] = 0

print(answer["L"], answer["R"])