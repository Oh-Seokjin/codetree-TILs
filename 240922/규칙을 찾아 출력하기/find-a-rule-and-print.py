n = int(input())

if n == 1:
    print("*")
else:     
    print("* "*n)

    for i in range(n-2):
        print("* " + "* "*i + "  "*(n-i-2) + "*")

    print("* "*n)