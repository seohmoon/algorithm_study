#BOJ 백준 1769번 3의 배수 

#새로운 함수 만들어서 재귀로 계속 돌리기
#ㄴ각 자리수의 합을 해줌

def baesoo(X):
    #cnt_num = 0
    sum_x = 0
    #result = ''
    #cnt_num += 1
    #while sum_x > 10:
    while X >= 10:
            #cnt_num += 1
        sum_x = baesoo(X // 10) + X % 10
            #리턴값으로 총 합을 반환해서 본식에서 처리해주자
        return(sum_x)
    
            
cnt_num = 0        
bs = baesoo(1234567)
while bs > 10:
    cnt_num += 1
    bs = baesoo(bs)
print(bs)

if bs % 3:
    print ('YES')
else :
    print ('NO')
    

    #return (cnt_num, result)

#for i in baesoo(1234567):
   # print (i)