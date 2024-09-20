tel = input()
former, latter = tel.split("-")[1], tel.split("-")[2]
print(f"010-{latter}-{former}")