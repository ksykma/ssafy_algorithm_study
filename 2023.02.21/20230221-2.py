# SW Expert Academy 0220_Queue - 1225 

import sys
sys.stdin = open('input.txt', 'r')

def enQueue(item):
    global rear
    rear = (rear + 1) % 9
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % 9
    return Q[front]


for t in range(1, 11):
    T = int(input())
    Q = [0] + list(map(int, input().split()))
    front = 0
    rear = 8
    cnt = 1
    while True:
        re = deQueue() - cnt
        if re <= 0:
            re = 0
            enQueue(re)
            print(f'#{t}', end = ' ')
            for i in range(8):
                print(deQueue(), end = ' ')
            print()
            break
        else:
            enQueue(re)
            cnt += 1
        if cnt == 6:
            cnt = 1
