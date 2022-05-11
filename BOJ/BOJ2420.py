#BOJ2420 사파리월드
N, M = map(int, input().split())
ans = N - M
if ans < 0:
    print(-ans)
else:
    print(ans)