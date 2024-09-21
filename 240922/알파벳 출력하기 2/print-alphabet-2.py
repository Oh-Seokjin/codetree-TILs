n = int(input())
cnt = ord("A")

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n - i): 
        print(chr(cnt), end=" ")

        cnt += 1 
        
        if cnt == 91:
          cnt = 65

    
    print()