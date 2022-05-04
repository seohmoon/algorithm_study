# BOJ17219 비밀번호 찾기
N, M = map(int, input().split())
pwdic = {}
for i in range(N):
    site, password = map(str, input().split())
    pwdic[site] = password
for j in range(M):
    j = input()
    print(pwdic[j])