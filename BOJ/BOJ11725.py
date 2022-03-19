# BOJ11725 트리의 부모 찾기
# 시간초과ㅜㅜ 

import sys

v = int(input()) # 정점
e = v - 1 # 간선
arr = []
for i in range(e):
    arr.append(list(map(int,sys.stdin.readline().split())))
    #arr.append(list(map(int, input().split())))
# arr을 다시 정렬해주기
newarr = []
for j in arr:
    if j[0] == 1: # 1일 때 루트
        newarr += [j]
    elif j[1] == 1:
        j[0], j[1] = j[1], j[0]
        newarr += [j]
newarr = sorted(newarr, key= lambda x : x[1])
#print(newarr) # x[1] 오름차순 정렬
tem = 0
#print(arr)
while tem <= v:    
    for a in arr:
        if a not in newarr:
            if a[0] == newarr[tem][1]:
                newarr += [a]
            elif a[1] == newarr[tem][1]:
                a[0], a[1] = a[1], a[0]
                newarr += [a]
    tem += 1
#print(newarr)
par = [0] * (v+1)
for b in newarr:
    #print(b)
    p = b[0]
    c = b[1]
    if par[c] == 0:
        par[c] = p
#print(par)
for d in par:
    if d != 0:
        print(d)