# BOJ9375 패션왕 신해빈
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    clothes = []
    for i in range(N):
        clothes.append(list(map(str, input().split())))