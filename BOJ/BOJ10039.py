# BOJ10039 평균점수
score = []
for i in range(5):
    i = int(input())
    if i >= 40:
        score.append(i)
    else:
        score.append(40)
ans = sum(score) // 5
print(ans)