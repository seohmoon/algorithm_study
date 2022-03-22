# BOJ11659 구간 합 구하기
# 투포인터로 풀어도 되고, 누적합으로 풀어도 됩니당

# 누적합
from sys import prefix


N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)] # N+1인 이유는 앞에 패딩

for i in range(1, N+1):
    prefix[i] = prefix[i - 1] + arr[1]

for j in range(M):
    a, b = map(int, input().split())

    print(prefix[b] - prefix[a - 1])



'''
import sys
얘는 시간초과ㅠ

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for a in range(M):
    i, j = map(int, sys.stdin.readline().split())
    total = 0
    if i == j:
        total = arr[i-1]
    else :
        for b in range(i-1, j):
            total += arr[b]
    print(total)
    '''