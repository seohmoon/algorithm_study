# BOJ 2805 나무 자르기
import sys

def check(x):
    ans = 0
    for i in trees:
        if i > x:
            ans += i-x
    return ans >= M


N, M = map(int, input().split())
trees = list(map(int,sys.stdin.readline().split()))

s = 0
e = 1000000000 # 문제에서 가장 큰 수 주어짐
ans = 0
while s <= e:
    mid = (s+e)//2
    if check(mid): # True일 때
        ans = mid
        s = mid + 1
    else: # False 일 때
        e = mid - 1
print(ans)