# BOJ 2581 소수
def sosoo(x):
    global all
    global minnum
    for i in range(2, x):
        if x % i == 0:
            return False
    all += x
    if minnum == 0:
        minnum = x
    return True

M = int(input())
N = int(input())
all = 0
minnum = 0
for i in range(M, N+1):
    sosoo(i)
if all == 0:
    print("-1")
else:
    print(all)
    print(minnum)