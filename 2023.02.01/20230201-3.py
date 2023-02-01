# SW Expert Academy 0201_List01 - 12384
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_val = 0
    min_val = 1000000
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    print(f"#{t} {max_val - min_val}")
