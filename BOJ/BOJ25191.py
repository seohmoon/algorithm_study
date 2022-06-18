# BOJ25191 치킨댄스를 추는 곰곰이를 본 임스
N = int(input())
A, B= map(int, input().split())
ans = 0
ans += A//2
ans += B
if ans > N:
    print(N)
else:
    print(ans)