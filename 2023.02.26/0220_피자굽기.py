# SW Expert Academy 0220_Queue - 11650    

import sys
sys.stdin = open('input.txt', 'r')
def enqueue(item):
    global rear
    if front == (rear + 1) % (N + 1):
        return 0
    else:
        rear = (rear + 1) % (N + 1)
        Q[rear] = item

def dequeue():
    global front
    if isEmpty():
        return
    front = (front + 1) % (N + 1)
    return Q[front]

def isEmpty():
    return front == rear

    
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    Q = [0] * (N + 1)
    pizza = []
    front = 0
    rear = 0
    for i in range(M):
        pizza.append([C[i], i+1])
    for i in range(N):
        enqueue(pizza[i])
    next = N
    while not isEmpty():
        [p, c] = dequeue()
        result = c
        p = p // 2
        if p:
            enqueue([p, c])
        else:
            if next < M:
                enqueue(pizza[next])
                next += 1
    print(f'#{t}', result)