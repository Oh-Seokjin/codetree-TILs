# code by "alsry922"

x = int(input())

curr_pos = 0
curr_speed = 1
sum_time = 0

while True:
    curr_pos += curr_speed
    sum_time += 1
    curr_speed+= 1

    if curr_pos == x:
        break
    
    increase_sum = 0
    for i in range(curr_speed):
        increase_sum += i
    if x-(curr_pos+curr_speed) < increase_sum:
        curr_speed -= 1

    stay_sum = 0
    for i in range(curr_speed):
        stay_sum += i
    if x-(curr_pos+curr_speed) < stay_sum:
        curr_speed -= 1

print(sum_time)