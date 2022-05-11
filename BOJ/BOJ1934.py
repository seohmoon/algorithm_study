# BOJ1934 최소공배수
# 시간초과
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    while True:
        n = 1
        if (B * n) // A == 0:
            print(B*n)
            break
        n += 1