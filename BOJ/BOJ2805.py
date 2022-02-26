# BOJ 2805 나무 자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

for i in range(trees[-2]+1,-1,-1):
    tem = 0
    for j in trees:
        if j > i:
            tem += j - i
    if tem >= M:
        print(i)
        break

a = trees[N//2]
while True:
    tem = 0
    for j in trees:
        if j > a:
            tem += j - a
    if tem >= M:
        
