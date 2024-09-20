a, b, c = map(int, input().split())
added = a+b+c
avg = int(added/3)
result = added-avg
print(f"{added}\n{avg}\n{result}")