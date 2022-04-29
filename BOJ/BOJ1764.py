# BOJ1764 듣보잡
# 시간초과
N, M = map(int, input().split())
Nlist = []
for i in range(N):
    Nlist.append(input())
Mlist = []
for j in range(M):
    Mlist.append(input())
Nlist.sort()
Mlist.sort()
ans = []
for ii in Nlist:
    for jj in Mlist:
        if ii == jj:
            ans.append(ii)
            break
        if ii < jj:
            break
print(len(ans))
print(*ans, sep="\n")



