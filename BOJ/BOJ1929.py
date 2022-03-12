# BOJ1929 소수 구하기 
# M이상 N이하의 소수를 모두 출력하는 프로그램

from tabnanny import check


def prime_num(x):
    for i in range(3,x):
        if x % i == 0:
            re



M, N = map(int, input().split())
arr = [2, 3]
for a in range(5,N,2):
    check = 0
    for b in range(3,a):
        if a % b == 0:
            check = 1
            break
    if check == 0:
        arr.append(a)

for i in range(M,N+1):
    check2 = 0
    for j in arr:
        if i % j == 0:
            check2 = 1
            break
    if check == 0:
        print(i)
