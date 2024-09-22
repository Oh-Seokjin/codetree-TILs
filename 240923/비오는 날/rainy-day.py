n = int(input())
near_date = ["9999-99-99"]
near_day = [""]

for i in range(n):
    date, day, weather = input().split()
    if weather != "Rain":
        continue

    if near_date[0] >= date:
        near_date.pop()
        near_date.append(date)
        near_day.pop()
        near_day.append(day)

print(f"{near_date[0]} {near_day[0]} Rain")