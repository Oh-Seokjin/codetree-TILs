def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], n-1):
            result.append([elem]+rest)
    return result   

team = list(map(int, input().split()))
combination_team = combination(team, 2)

flag = 0
diff = 9999

for team_a in combination_team:
    rest = [elem for elem in team if elem not in team_a]
    combination_b = combination(rest, 2)
    
    for team_b in combination_b:
        team_c = [elem for elem in rest if elem not in team_b]
        
        capa = [sum(team_a),sum(team_b), sum(team_c)]

        if len(set(capa)) != 3:
            continue
        
        temp_diff = max(capa) - min(capa)
        if temp_diff < diff:
            diff = temp_diff
            flag = 1
    
if flag:
    print(diff)
else:
    print(-1)