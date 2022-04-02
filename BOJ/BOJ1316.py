# BOJ1316 그룹단어 체커

def groupnum(x):
    alphabet = []
    for i in x:
        if i not in alphabet:
            alphabet.append(i)
        else:
            if i != alphabet[-1]:
                return False
    return True

N = int(input())
cnt = 0
for i in range(N):
    word = input()
    if groupnum(word):
        cnt += 1
print(cnt)