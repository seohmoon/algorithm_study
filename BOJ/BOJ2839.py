# BOJ2839 설탕배달
n = int(input())
a = n // 5
if n == 7: # n이 7일때
    print(-1)
     
if n % 5 == 0: # 5의 배수
    print(a)
    
if n == 3:
     # n이 3일때
    print(1)
    
if n == 4:
     # n이 4일때
    print(-1)
     
while True:
    #if n == 7: # n이 7일때
     #   print(-1)
      #  break 
    #if n % 5 == 0: # 5의 배수
     #   print(a)
      #  break
    #if a == 0:
     #   if n == 3: # n이 3일때
      #      print(1)
       #     break
        #elif n == 4: # n이 4일때
         #   print(-1)
          #  break    
    if a >= 0:
        b = n % 5 # 5로 나눈 나머지로 3kg짜리 갯수 확인
        if b % 3 == 0:
            print(a + b//3)
            break
        else:
            a -= 1
            b += 5
            if b % 3 ==0:
               print(a + b//3)
               break