# 백준 2564 경비원

import sys
sys.stdin = open('input.txt', 'r')

# 1 : 북 2 : 남 3 : 서 4 : 동

def function(x, y):
    if x == 1:
        return y
    if x == 2:
        return W + H + W - y
    if x == 3:
        return W + H + W + H - y
    if x == 4:
        return W + y

W, H = list(map(int, input().split()))
N = int(input())

store = []
for _ in range(N + 1):
    x, y = map(int, input().split())
    store.append(function(x, y))

result = 0
for i in range(N):
    a = abs(store[-1] - store[i])
    b = 2 * (W + H) - a
    result += min(a, b)

print(result)