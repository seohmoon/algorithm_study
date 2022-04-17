# BOJ 2581 소수
M = int(input())
N = int(input())
all = 0
minnum = 0
for i in range(M, N+1):
    pn = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            pn = False
            break
    if pn:
        if minnum == 0:
            minnum = i
        all += i

if all == 0:
    print(-1)
else:
    print(all)
    print(minnum)   