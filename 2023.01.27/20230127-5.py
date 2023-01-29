import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int,input().split()))
    number = 0
    for j in numbers:
        if j > number:
            number = j
    print(f"#{i} {number}")