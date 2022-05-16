# BOJ5635 생일
N = int(input())
lst = []
for tc in N:
    tc = list(map(str, input().split()))
lst.sort(key=lambda x:lst[[-1]])

