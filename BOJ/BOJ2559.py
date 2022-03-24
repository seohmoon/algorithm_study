# BOJ2559 수열
# 누적합

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix = [0 for _ in range(N+1)] # 누적합

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i]

maxtem = -100*K # 가장 작은 값 써주기
for j in range(K, N+1): # 차이
    if prefix[j] - prefix[j-K] > maxtem:
        maxtem = prefix[j] - prefix[j-K]

print(maxtem)
