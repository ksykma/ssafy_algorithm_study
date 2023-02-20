# SW Expert Academy 0220_Queue - 11649 

import sys
sys.stdin = open('input.txt', 'r')

def enQueue(item):
    global rear
    if isFull():
        return
    else:
        rear += 1
        pizza[rear] = item

def deQueue():
    global front
    if isEmpty():
        return
    else:
        front += 1
        return pizza[front]

def isFull():
    return rear == len(pizza) - 1

def isEmpty():
    return rear == front

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))   # N : 화덕 크기, M : 피자 개수
    C_lst = list(map(int, input().split()))   # 치즈의 양
    pizza = [0] * N
    front = -1
    rear = -1
    for i in C_lst:
        enQueue(i)
    while True:
        for i in range(N):
            if pizza[i] == 1:
                deQueue()
            else:
                pizza[i] = pizza[i] // 2