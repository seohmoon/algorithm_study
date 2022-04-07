# BOJ 11047 동전 0 
N, K = map(int, input().split())
arr= []
cnt = 0
for i in range(N):
    i = int(input())
    arr.append(i)
arr= arr[::-1]
for j in arr:
    tem = K // j
    if tem != 0:
        cnt += tem
    K -= tem*j
print(cnt)