# BOJ2798 블랙잭
N, M = map(int, input().split())
arr = list(map(int, input().split()))
tem = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k] <= M:
                if tem < arr[i]+arr[j]+arr[k]:
                    tem = arr[i]+arr[j]+arr[k]
print(tem)