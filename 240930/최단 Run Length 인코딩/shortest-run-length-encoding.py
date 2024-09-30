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
        temp = run[-1]
        run = [temp] + run[:-1]
    
    search = run[0]
    cnt = 1
    for i in range(1, len(run)):
        if run[i] == search:
            cnt += 1
        else:
            rle = rle + search + str(cnt)
            search = run[i]
            cnt = 1
        if i == len(run)-1:
            rle = rle + search + str(cnt)
            
print(len(rle))