# 백준 2479 경로 찾기

import sys
sys.stdin = open('input.txt', 'r')

score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

score_list = [list(input().split()) for _ in range(20)]
result_sum = 0
score_sum = 0
for i in range(20):
    if score_list[i][2] != 'P':
        result_sum += float(score_list[i][1]) * float(score[score_list[i][2]])
        score_sum += float(score_list[i][1])
print("{:6f}".format(result_sum / score_sum))