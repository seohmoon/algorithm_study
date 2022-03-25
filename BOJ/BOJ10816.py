# BOJ10816 숫자카드2
import sys

def cnt_idx(x):
    global nrr
    cnt = 0
    n = 1
    while True:
        if x-n >= 0 and nrr[x] == nrr[x-n]:
            cnt += 1
            n += 1
        else:
            break
    n = 1    
    while True:
        if x+n <= len(nrr)-1 and nrr[x] == nrr[x+n]:
            cnt += 1
            n += 1
        else:
            break
    return (cnt)


N = int(sys.stdin.readline())
nrr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
mrr = list(map(int,sys.stdin.readline().split()))
nrr.sort()
# 이진탐색

for i in mrr:
    s = 0
    e = N -1
    ans = 0     
    while s <= e: 
        mid = (s+e) // 2
        if i == nrr[mid]:
            ans = 1
            ans += cnt_idx(mid)
            break 
        elif i > nrr[mid]:
            s = mid + 1
        elif i < nrr[mid]:
            e = mid - 1
    print(ans, end=" ")
    '''        
    s = 0
    e = N -1      
    while s <= e: # 가장 큰 인덱스
        mid = (s+e) // 2
        if i == nrr[mid]:
            idx2 = mid
            ans = 1
            s = mid + 1 
        elif i > nrr[mid]:
            s = mid + 1
        elif i < nrr[mid]:
            e = mid - 1
    if ans == 0:
        print(0, end=" ")
    else:
        print(idx2 - idx1 + 1, end= " ")
'''

''' 시간초과
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
'''
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