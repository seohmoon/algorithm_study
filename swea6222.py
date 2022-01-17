a = input()
b = ord(a)
if 97 <= b <= 122:
    print(f'{a}(ASCII: {b}) => {chr(b-32)}(ASCII: {b-32})')
elif 65 <= b <= 90:
    print(f'{a}(ASCII: {b}) => {chr(b+32)}(ASCII: {b+32})')
else:
	print(a)
#SWEA6222번 대소문자 변환