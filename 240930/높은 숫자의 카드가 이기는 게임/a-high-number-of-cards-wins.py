n = int(input())
cards = [i for i in range(1, 2*n+1)]
###

# print(cards)
cnt = 0

for _ in range(n):
    b = int(input())
    cards.pop(cards.index(b))
    for i in range(b+1, 2*n+1):
        if i in cards:
            cards.pop(cards.index(i))
            cnt += 1
            break
        else:
            continue

print(cnt)