#재귀함수 백준 10829번 이진수 변환
'''
n = int(input())
print(bin(n)[2:])
'''

'''
#재귀함수로 풀어볼게
def leejinsoo(n):
    if n >= 2:
        a = n % 2
        result = leejinsoo(n // 2) + str(a)
        return (result)
    elif n < 2:
        return(str(n))

print(leejinsoo(53))
#n = int(input())

#str(a)로 쓴건 int로 반환하면 숫자가 더해지기 때문
'''
