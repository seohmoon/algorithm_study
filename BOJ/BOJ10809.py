# BOJ 10809번 알파벳 찾기

words = input()
j = 0

for i in range(0,26):
    tem = chr(97+j)
    a = words.count(tem)
    j += 1
    if a == 0:
        print(-1, end =' ')
    else :
        print(words.index(tem), end=' ')