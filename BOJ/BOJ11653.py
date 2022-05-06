# BOJ11653 소인수분해
N = int(input())
if N != 1:
    tem = 2
    while N > 1:
        if N % tem == 0:
            print(tem)
            N = N // tem
        else:
            tem += 1