# BOJ 2884 알람 시계
H, M = map(int, input().split())
# 45분 전으로 바꾸기
if M >= 45:
    M -= 45
else:
    if H == 0:
        H = 23
    else :
        H -= 1
    M -= 45
    M += 60
print(H, end=" ")
print(M)