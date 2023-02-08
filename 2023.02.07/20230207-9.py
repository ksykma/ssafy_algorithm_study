# SW Expert Academy 0207_List02 - 1954

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # num = 1
    # dr = [0, 0, 1, 0, -1]
    # dc = [0, 1, 0, -1, 0]
    # a = 0
    # for i in range(N):
    #     for j in range(N):
    #         ni = i + dr[a]
    #         nj = j + dc[a]
    #         arr[ni][nj] = num
    #         num += 1
    #          # 어떤 조건을 만났다! -> dr, dc의 인덱스를 다음으로 +1
    #         if ni >= N or nj >= N:
    #             a += 1
    #             if a >= 5:
    #                 a = 1


    trans = 1
    cnt = 1
    row, col = 0, -1

    while N > 0:
        for i in range(N):  # ->, <- (col)
            col += trans
            arr[row][col] = cnt
            cnt += 1

        N -= 1		# 첫 번째 외 2번씩 같은 칸 수 이동

        for i in range(N):  # 아래, 위 (row)
            row += trans
            arr[row][col] = cnt
            cnt += 1

        trans *= -1	  # 증가/감소 방향 변경
                        

    for line in arr:
        print(*line)

