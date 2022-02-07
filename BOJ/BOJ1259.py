# BOJ 1259 팰린드롬수

def radar(num):
    if num == num[::-1]:
        return('yes')
    else:
        return('no')
  
#num = str(input())
while True:
    num = str(input())
    if num == '0':
        break
    else:
        print(radar(num))