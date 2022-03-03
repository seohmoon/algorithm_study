# BOJ11659 구간 합 구하기
import sys

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