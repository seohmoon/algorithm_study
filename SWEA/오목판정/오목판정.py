# SWEA11315 오목판정
import sys
sys.stdin = (open("sample_input.txt"))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
