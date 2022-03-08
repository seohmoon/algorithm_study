# BOJ4344 평균은 넘겠지
C = int(input())
for tc in range(C):
    arr = list(map(int, input().split()))
    # 평균 구하기
    total = 0
    for i in range(1,len(arr)):
        total += arr[i]
    a = total//arr[0] # 얘가 평균

    # 평균 넘는 학생 찾기
    cnt = 0
    for j in range(1, len(arr)):
        if arr[j] > a:
            cnt += 1
    
    # 비율 구하기
    print('%.3f' % (cnt / arr[0] * 100) + '%')
