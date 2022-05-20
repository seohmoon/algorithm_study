# BOJ10824 네 수
A, B, C, D= map(str, input().split())
A += B
C += D
A = int(A)
C = int(C)
print(A+C)