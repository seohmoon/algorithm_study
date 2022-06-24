# BOJ5988 홀수일까 짝수일까
N = int(input())
for i in range(N):
    i = int(input())
    if i % 2 == 0:
        print("even")
    else:
        print("odd")