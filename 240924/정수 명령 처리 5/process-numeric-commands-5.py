n = int(input())
arr = []
for _ in range(n):
    order = input()
    if order == "size":
        print(len(arr))
        continue
    elif order == "pop_back":
        arr.pop()
        continue

    order, value = order.split()
    value = int(value)

    if order == "push_back":
        arr.append(value)
    elif order == "get":
        print(arr[value-1])