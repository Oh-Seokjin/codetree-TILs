n = int(input())
nine = "987654321"

for i in range(1, n**2+1):
    print(nine[(i-1)%9], end="")
    if i%4 == 0:
        print()