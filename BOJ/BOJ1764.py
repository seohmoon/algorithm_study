# BOJ1764 듣보잡
# 시간초과
import sys

N, M = map(int, input().split())
Nlist = [sys.stdin.readline().strip() for i in range(N)]
Mlist = [sys.stdin.readline().strip() for j in range(M)]

ans = list(set(Nlist) & set(Mlist))

print(len(ans))
print(*ans, sep='\n')