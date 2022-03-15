# BOJ10816 숫자카드2
import sys
N = int(sys.stdin.readline())
nrr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mrr = list(map(int,sys.stdin.readline().split()))
nrr.sort()

for i in range(M):
    before = 0
    cnt = 0
    if i == 0:
        for j in range(N):
            if mrr[i] == nrr[j]:
                cnt += 1
                before = j
            elif mrr[i] < nrr[j]:
                break
    else:
        if mrr[i] == mrr[i-1]:
                cnt += 1
        elif mrr[i] > mrr[i-1]:          
            for j in range(before, N):
                if mrr[i] == nrr[j]:
                    cnt += 1
                    before = j
                elif mrr[i] < nrr[j]:
                    break
        elif mrr[i] < mrr[i-1]:
            for j in range(N):
                if mrr[i] == nrr[j]:
                    cnt += 1
                    before = j
                elif mrr[i] < nrr[j]:
                    break
    print(cnt, end=" ")

''' 시간초과
N = int(input())
nrr = list(map(int, input().split()))
M = int(input())
mrr = list(map(int, input().split()))
nrr.sort()

for i in mrr:
    cnt = 0
    for j in nrr:
        if i == j:
            cnt += 1
        elif i < j:
            break
    print(cnt, end=" ")

'''