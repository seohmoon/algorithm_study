# BOJ10797 10부제
N = int(input())
cars = list(map(int, input().split()))
ans = 0
for i in cars:
    if i == N:
        ans += 1
print(ans)
