# 백준 15989 1, 2, 3 더하기 4

N = int(input())

lst = [1] * 10001 # 모든 값을 1로 만드는 경우는 1가지 이므로 기본값 1

for i in range(2, 10001): # 2부터 10000까지의 숫자의 경우의 수
    lst[i] += lst[i - 2] # lst[i]에 i에서 2를 뺀 숫자의 경우의 수를 더해줌
    
for i in range(3, 10001):
    lst[i] += lst[i - 3]

for i in range(N):
    n = int(input())
    print(lst[n])