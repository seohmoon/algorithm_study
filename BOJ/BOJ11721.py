#BOJ11721 열 개씩 끊어 출력하기
lst = list(map(str,input()))
for i in range(len(lst)):
    if i != 0 and i % 9 == 0:
        print(lst[i])
    else:
        print(lst[i], end="")
