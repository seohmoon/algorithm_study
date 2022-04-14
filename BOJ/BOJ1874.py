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
ans = []
while stack:
    stack2.append(stack.pop())
    ans.append("+")
    if tem == n:
        break
    while True:
        if stack2 != [] and tem < n and stack2[-1] == randominput[0+tem]:
            stack2.pop()
            tem += 1
            ans.append("-")
            if tem == n:
                break
        else:
            break
if  tem == n:
    print(*ans, sep="\n")
else:
    print("NO")
    