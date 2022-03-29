# BOJ10828 스택
import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    word = list(map(str, sys.stdin.readline().split()))
    if len(word) == 2:
        word[-1] = int(word[-1])
    if word[0] == 'push':
        stack.append(word[-1])
    elif word[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif word[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])