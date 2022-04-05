# BOJ1010 다리 놓기

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tem = 0
    up = 1
    downn = 1
    for i in range(N):
        up *= (M - i)
    for j in range(1, N+1):
        downn *= j
    print(up // downn)
    

    