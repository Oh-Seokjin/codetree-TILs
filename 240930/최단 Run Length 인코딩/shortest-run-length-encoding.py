text = input()
###
run = [s for s in text]

rle = ""

if len(set(run)) == 1:
    cnt = str(run.count(run[0]))
    rle = run[0]+cnt
else:
    while True:
        if run[0] != run[-1]:
            break
        temp = run[0]
        run = run[1:] + [temp]
    for elem in set(run):
        rle = rle + elem + str(run.count(elem))

print(len(rle))