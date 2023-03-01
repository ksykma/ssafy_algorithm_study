# SW Expert Academy 0227_Start - 1242

import sys
sys.stdin = open('input.txt', 'r')

dict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
dict_2 = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
          '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
          '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
          'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'}
check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
 
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]
    lst = []
    # arr을 for문을 돌려 한줄에 check에 존재하는 문자가 존재하면 해당 줄의 오른쪽 0들을 제거 후 lst에 추가
    for i in range(N):
        for j in check:
            if j in arr[i]:
                a = arr[i].strip().rstrip('0')
                if a not in lst:
                    lst.append(a)
    lst2 = []
    # lst를 for문을 돌려 한줄을 뽑고
    for i in range(len(lst)):
        num = ''
        # 그 한줄을 for문을 돌려 1글자로 만들어 해당 문자를 dict_2의 키값으로 하여 value값을 가져와 num에 붙이기
        for j in range(len(lst[i])):
            num += dict_2[lst[i][j]]
        # num의 오른쪽의 0을 모두 제거 후 lst2에 추가
        lst2.append(num.strip().rstrip('0'))
 
    lst3 = []
    # lst2를 for문을 돌려 한줄을 뽑고
    for i in range(len(lst2)):
        # 0에서 1로, 1에서 0으로 바뀌는 횟수를 카운트하기 위해 plus 활용
        plus = 0
        length = len(lst2[i])-1
        # lst2[i]가 빌때까지 돌려
        while lst2[i]:
            # lst2[i]의 뒤에서부터 length번째 문자와 length-1번째 문자가 다르면 plus에 1 추가
            if lst2[i][length] != lst2[i][length-1]:
                plus += 1
                # plus가 31이 되면 lst3에 lst2[i][length:] 문자열을 추가
                if plus == 31:
                    put = str(lst2[i][length:])
                    lst3.append(put.strip().lstrip('0'))
                    # lst2[i]는 앞의 put을 자른 후 남은 문자열에서 오른쪽에 존재하는 0을 모두 제거한 문자열만 저장
                    lst2[i] = str(lst2[i][:length]).strip().rstrip('0')
                    # lst2[i]의 길이도 새로 조정
                    length = len(lst2[i])-1
                    # plus 초기화
                    plus = 0
            # while문 돌릴때마다 1씩 줄여주기
            length -= 1
    # lst3을 for문을 돌려 한줄을 뽑고
    n = 1
    for i in range(len(lst3)):
        while True:
            # 해당 줄의 길이가 56*n보다 크면 n에 1 추가 
            if len(lst3[i]) > 56*n:
                n += 1
            # 해당 줄의 길이가 56*n보다 작거나 같으면 해당 줄의 길이가 56*n이 되도록 zfill로 앞부분에 0 채워주기
            else:
                lst3[i] = lst3[i].zfill(56*n)
                # n을 1로 초기화
                n = 1
                break
 
    lst4 = []
    # lst3을 for문을 돌려 한줄을 뽑고
    for i in range(len(lst3)):
        result = ''
        # 해당 줄이 56의 몇배수인지 알아내기
        mok = len(lst3[i]) // 56
        # 해당 줄의 비율을 조정
        for j in range(0, len(lst3[i]), mok):
            result += lst3[i][j]
        lst4.append(result)
    # 중복되는 값 제거
    lst4 = list(set(lst4))
    
    # lst4를 for문을 돌려 한줄을 뽑고
    ans = 0
    for i in range(len(lst4)):
        left = []
        right = []
        # 해당 줄을 7개씩 잘라서 dict의 키값으로하여 value값 불러오기
        for j in range(0, len(lst4[i]), 7):
            jjin = dict[lst4[i][j:j+7]]
            # 홀수이면 left에 짝수이면 right에 추가
            if (j+1) % 2 == 1:
                left.append(jjin)
            else:
                right.append(jjin)
        # left을 모두 더한 값 * 3 + right을 모두 더한 값이 10의 배수이면
        if ((sum(left) * 3) + sum(right)) % 10 == 0:
            # left을 모두 더한 값 + right을 모두 더한 값을 ans에 더하기
            ans += sum(left) + sum(right)
    print(f'#{t}', ans)