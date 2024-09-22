n = int(input())

str_list = []
answer_list = []

for _ in range(n):
    str_list.append(input())

goal_chr = input()

for elem in str_list:
    if elem.startswith(goal_chr):
        answer_list.append(elem)

len_str = 0
for elem in answer_list:
    len_str += len(elem)

print(f"{len(answer_list)} {len_str/len(answer_list):.2f}")