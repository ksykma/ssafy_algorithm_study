# 백준 1713 후보 추천하기

import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 사진틀 개수
C = int(input()) # 전체 추천 횟수
recommend = list(map(int, input().split()))
picture = []
# lst.sort(key=lambda x:x[0])
for i in range(C): # 게시 순서, 학생 번호, 추천 수
    if i <= N-1:
        picture.append([i, recommend[i], 1])
    else:
        picture.sort(key=lambda x:(x[2], x[0]))
        for j in range(N):
            if recommend[i] == picture[j][1]:
                picture[j][2] += 1
                break
        else:
            picture[0] = [i, recommend[i], 1]

picture.sort(key=lambda x:x[1])
for i in range(N):
    print(picture[i][1], end=' ')
