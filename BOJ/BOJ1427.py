# BOJ1427 소트인사이드
arr = list(map(str, input()))
arr.sort()
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end="")
