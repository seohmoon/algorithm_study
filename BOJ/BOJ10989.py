# BOJ10989 수정렬하기3
N = int(input())

cnt = [0 for i in range(10001)]

for j in range(N):
    j = int(input())
    cnt[j] += 1

for a in range(len(cnt)):
    for b in range(cnt[a]):
        if cnt[a] != 0:
            print(a)

'''시간초과
N = int(input())
arr = []
for i in range(N):
    if arr == []:
        arr.append(int(input()))
    else :
        arr.append(int(input()))
        for j in range(i):
            if arr[-1-j] < arr[-2-j]:
                arr[-1-j], arr[-2-j] = arr[-2-j], arr[-1-j]
            else:
                break
for k in arr:
    print(k)
    '''