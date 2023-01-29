import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int,input().split()))
    sum_num = 0
    for j in numbers:
        sum_num += j
    result = round(sum_num / 10)
    print(f"#{i} {result}")