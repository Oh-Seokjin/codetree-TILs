total_age = 0
cnt = 0
while True:
    age = int(input())
    if age >= 30 or age < 20:
        break
    total_age += age
    cnt += 1
print(f"{total_age/cnt:.2f}")