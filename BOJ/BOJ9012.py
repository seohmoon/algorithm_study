# BOJ9012
from unittest import result


T = int(input())
for i in range(T):
    arr = map(str, input())
    stack = []
    result = 0
    for j in arr:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack != []:
                stack.pop()
            elif stack == []:
                result = 1
                break

    if result == 1:
        print("NO")
    elif stack != []:
        print("NO")
    elif result == 0 and stack == []:
        print("YES")
