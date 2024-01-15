# 백준 5073 삼각형과 세 변

import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# print(input)
while True:
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        break
    elif a == b == c:
        print("Equilateral")
    elif max(a, b, c) >= a + b + c - max(a, b, c): # 가장 긴 변이 나머지 변 더한 값보다 길거나 같은지
        print("Invalid")
    elif (a == b) or (a == c) or (b == c):
        print("Isosceles")
    else:
        print("Scalene")
        
    # if문 순서도 중요했다!!