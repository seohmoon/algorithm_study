# BOJ5585 거스름돈
N = int(input())
ans = 0
# 500, 100, 50, 10, 5, 1 중 거스름돈 갯수 가장 적게
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    if coin <= N:
        