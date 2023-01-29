import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int,input().split()))
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j + 1]:
            print(f"#{i} >")
        elif numbers[j] == numbers[j + 1]:
            print(f"#{i} =")
        if numbers[j] < numbers[j + 1]:
            print(f"#{i} <")