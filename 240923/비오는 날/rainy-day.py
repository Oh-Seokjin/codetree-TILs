n = int(input())
near_date = ["9999-99-99"]
near_day = [""]

for i in range(n):
    date, day, weather = input().split()
    if weather != "Rain":
        continue
    p_y, p_m, p_d = map(int, near_date[0].split("-"))
    c_y, c_m, c_d = map(int, date.split("-"))
    if c_y <= p_y and c_m <= p_m and c_d <= p_d:
        near_date.pop()
        near_date.append(date)
        near_day.pop()
        near_day.append(day)

print(f"{near_date[0]} {near_day[0]} Rain")