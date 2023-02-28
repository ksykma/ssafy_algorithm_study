import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

code_table = {
    (0, 0, 0, 1, 1, 0, 1) : 0,
    (0, 0, 1, 1, 0, 0, 1) : 1,
    (0, 0, 1, 0, 0, 1, 1) : 2,
    (0, 1, 1, 1, 1, 0, 1) : 3,
    (0, 1, 0, 0, 0, 1, 1) : 4,
    (0, 1, 1, 0, 0, 0, 1) : 5,
    (0, 1, 0, 1, 1, 1, 1) : 6,
    (0, 1, 1, 1, 0, 1, 1) : 7,
    (0, 1, 1, 0, 1, 1, 1) : 8,
    (0, 0, 0, 1, 0, 1, 1) : 9,
    }
def find_code():
    global ans
    # 행 우선 순회로
    for r in range(N):
        for c in range(M - 1, 55, -1):
            # 뒤에서부터 검사하면
            # 1을 만났을 때 코드가 되는 부분을 볼 수 있다.
            # 앞에서부터 검사하면
            # 코드가 0부터 시작하고, 코드가 없는 부분도 0으로 되어있기 때문에
            # 모든 c에 대해서 검사를 해야한다.
            
            # 뒤에서부터 56개를 잘라보자.
            code = arr[r][c:c - 56:-1]
            # 자른 코드의 맨 앞을 보고 1이면 코드가 될 수 있음
            # 0이면 코드가 될 수 없다 => ?? 코드는 모두 1로 끝난다.
            if code[0] != 1:
                continue
            # 현재 행 r에서 시작해서 5개가 다 똑같은지 검사
            for nr in range(r, r + 5):
                ncode = code
                if ncode != code:
                    break
            # 만약 중간에 break 된 적이 없다. ==> 5줄이 동일
            else:
                # 여기서 코드를 제작
                code = code[ : : -1]
                # 뒤집고 나서 7개씩 8번 쪼갠다.
                # 홀수 * 3, 짝수는 그냥 +
                code_valid = 0
                # 위의 결과 10의 배수이면 숫자를 더하기
                code_sum = 0
                for i in range(8):
                    ni = 7 * i
                    # 코드를 해독한 결과가 테이블(딕셔너리)안에 존재하면
                    # 숫자 코드 완성
                    # 딕셔너리 안에 없으면? 만들기 중단하고
                    decode = code_table.get(tuple(code[ni:ni+7]))
                    if decode == None:
                        break
                    else:
                        # 코드에 맞는 숫자를 찾았다.
                        # 홀수번째 => * 3 (인덱스는 짝수)
                        # 짝수번째 -> + (인덱스는 홀수)
                        code_sum += decode
                        if i % 2 == 0:
                            code_valid += decode * 3
                        else:
                            code_valid += decode
                else:
                    # 주어진 식의 결과를 통해 10의 배수이면 코드 합격
                    if code_valid % 10 == 0:
                        ans = code_sum
                        return
            
for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    arr = [list(map(int, input())) for _ in range(N)]
    
    # 출력할 정답
    ans = 0
    find_code()
    
    print(f'#{t}', ans)