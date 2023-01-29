import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int,input().split()))
    result = 0
    for j in numbers:
        if j % 2 == 1:
            result += j
    print(f"#{i} {result}")