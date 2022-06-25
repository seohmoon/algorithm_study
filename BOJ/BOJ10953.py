# BOJ10953 
T = int(input())
for i in range(T):
    lst = list(map(str, input().split()))
    a = int(lst[0])
    b = int(lst[-1])
    print(a+b)