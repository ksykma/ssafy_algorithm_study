# SW Expert Academy 0220_Queue - 11649 

import sys
sys.stdin = open('input.txt', 'r')

def enQueue(item):
    global rear
    if front == (rear + 1) % (N + 1):
        return 0
    else:
        rear = (rear + 1) % (N + 1)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        return 0
    else:
        front = (front + 1) % (N + 1)
        return Q[front]

def isEmpty():
    return rear == front

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))   # N : 화덕 크기, M : 피자 개수
    C_lst = list(map(int, input().split()))   # 치즈의 양
    Q = [0] * (N + 1)
    pizza = []
    front = 0
    rear = 0
    for i in range(M):
        pizza.append([C_lst[i], i + 1])
    for i in range(N):
        enQueue(pizza[i])

    next = N
    while not isEmpty():
        [p, c] = deQueue()
        result = c
        p = p // 2
        if p:
            enQueue([p, c])
        else:
            if next < M:
                enQueue(pizza[next])
                next += 1

    print(f'#{t} {result}')

    