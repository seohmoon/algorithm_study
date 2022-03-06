# SWEA4874 Forth
import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    s = list(map(str, input().split()))
    # 피연산자 스택
    stack = []
    for i in s:
        if i != "+" and i != "*" and i != "." and i != "-" and i != "/": # 숫자일 때
            stack.append(int(i))
        elif i == ".": # 반복문 종료
            break
        else: # 연산자 일 때
            b = stack.pop()
            if len(stack) == 0: # b 뽑고 나머지 스택에 숫자 남아있는지
                break # 없으면 반복문 종료
            a = stack.pop()
            if i == "+":
                stack.append(a+b)
            elif i == "*":
                stack.append(a*b)
            elif i == "-":
                stack.append(a-b)
            elif i == "/":
                if b == 0: # 0으로 나눌 때 예외 처리
                    break
                stack.append(a//b)

    if len(stack) == 1:
        result = stack.pop()
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} error")