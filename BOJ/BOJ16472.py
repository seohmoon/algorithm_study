# BOJ16472 고냥이 ㅠㅠㅠㅠ귀여워 
N = int(input())
words = input()
s = words[0]
e = words[-1]
maxlen = 0

for i in range(len(words)):
    tem = set(words)