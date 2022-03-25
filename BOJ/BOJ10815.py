# BOJ10815 숫자 카드
N = int(input())
sg = list(map(int, input().split()))
M = int(input())
mrr = list(map(int, input().split()))
sg.sort()

for i in mrr:
    s = 0
    e = N-1
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if i > sg[mid]:
            s = mid + 1
        elif i < sg[mid]:
            e = mid - 1
        elif i == sg[mid]:
            ans = 1
            break
    print(ans, end=" ")