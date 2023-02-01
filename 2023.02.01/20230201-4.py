# SW Expert Academy 0201_List01 - 11151
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = -400
    for i in range(N-1):
        if lst[i] + lst[i+1] > max_val:
            max_val = lst[i] + lst[i+1]
    print(f"#{t} {max_val}")