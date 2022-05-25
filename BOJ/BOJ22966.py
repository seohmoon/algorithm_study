# BOJ22966 가장 쉬운 문제를 찾는 문제
N = int(input())
lev = 0
ans = []
for i in range(N):
    q, l = map(str, input().split())
    if lev == 0:
        lev = l
        ans.append(q)
    else:
        if lev > l:
            lev = l
            ans.append(q)
print(ans[-1])