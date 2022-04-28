# BOJ11050 이항계수1
N, K = map(int, input().split())
# 1 ≤ N ≤ 10, 0 ≤ K ≤ N
if K == 0 or N == K: # 0팩토리얼 일 때
    print(1)
else:
    up = 1
    down = 1
    for i in range(K):
        up *= N-i
        down *= K-i
    print(up // down)