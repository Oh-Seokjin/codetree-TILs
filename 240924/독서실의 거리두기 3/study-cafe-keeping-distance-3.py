n = int(input())
seats = input()

seats = sorted(seats.split("1"), key=lambda x: len(x), reverse=True)

seats.append(seats[0][:len(seats[0])//2])
seats.append(seats[0][len(seats[0])//2+1:])
del seats[0]
seats.remove("")
seats.remove("")
seats.sort()
print(seats)
print(len(seats[0])+1)