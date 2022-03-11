import sys
sys.stdin = open("sample_input.txt")



T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = []

    for i in s:
        if i == ")":
            if stack and stack[-1] == "(": # 스택이 비어있지 않을때 마지막 요소 비교
                stack.pop()
            else:
                stack.append(i)
        if i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
        if i == "(":
            stack.append(i)
        if i == "{":
            stack.append(i)
    if stack: # 스택 안 요소가 남아있으면
        print(f"#{tc} 0")
    else: # 스택이 비어있으면 정상적으로 짝을 이룸
        print(f"#{tc} 1")
