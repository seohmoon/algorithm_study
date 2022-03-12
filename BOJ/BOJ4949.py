# BOJ4949 균형잡힌 세상

while True:
    arr = list(map(str, input()))
    if len(arr) == 1 and arr[0] == ".":
        break
    stack = []
    result = 0
    for j in arr:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack != []:
                a = stack.pop()
                if a == '[':
                    result = 1
                    break
            elif stack == []:
                result = 1
                break
        elif j == '[':
            stack.append(j)
        elif j == ']':
            if stack != []:
                b = stack.pop()
                if b == '(':
                    result = 1
                    break
            elif stack == []:
                result = 1
                break
    if result == 1:
        print("no")
    elif stack != []:
        print("no")
    elif result == 0 and stack == []:
        print("yes")