# BOJ2480
A, B, C = map(int, input().split())
if A == B and B == C:
    print(10000 + A*1000)
elif A == B or B == C or A == C:
    if A != B and A != C:
        print(1000 + B*100)
    elif B != A and B != C:
        print(1000 + A*100)
    elif C != A and C != B:
        print(1000 + B*100)
else:
    print(max(A, B, C)*100)