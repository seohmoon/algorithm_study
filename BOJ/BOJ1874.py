# BOJ 1874 스택수열
n = int(input())
stack = []
for i in range(n,0,-1):
    stack.append(i)
randominput = []
for j in range(n):
    randominput.append(int(input()))
stack2 = []
tem = 0
while tem <= n:
    if stack[-1] != randominput[-1-tem]:
        stack2.append(stack.pop)
        print("+")
    else:
        tem -= 1
        stack.pop
        print("-")
    