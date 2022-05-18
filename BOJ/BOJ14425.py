# BOJ14425 문자열 집합
N, M = map(int, input().split())
ans = []
nset = []
mset = []
ans = 0
for i in range(N):
    nset.append(input())
for j in range(M):
    mset.append(input())
    mset = set(mset)
    mset = list(mset)
for k in mset:
    for kk in nset:
        if k == kk:
            ans += 1
            break
print(ans)