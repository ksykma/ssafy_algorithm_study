# 비밀지도 - 2018 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=python3

def solution(n, arr1, arr2):
    lst1 = []
    lst2 = []
    answer = []
    for i in arr1:
        bin1 = str(bin(i))[2:]
        if len(bin1) < n:
            lst1.append(bin1.zfill(n))
        else:
            lst1.append(bin1)
    for j in arr2:
        bin2 = str(bin(j))[2:]
        if len(bin2) < n:
            lst2.append(bin2.zfill(n))
        else:
            lst2.append(bin2)
    for a in range(n):
        num = ''
        for b in range(n):
            if lst1[a][b] == '0' and lst2[a][b] == '0':
                num += ' '
            else:
                num += '#'
        answer.append(num)
    
    return answer


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))