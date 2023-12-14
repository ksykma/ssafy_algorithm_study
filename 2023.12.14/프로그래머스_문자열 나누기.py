def solution(s):
    answer = 0 # 결과값
    word = s # 잘라낼 s값 저장
    a = 1 # 시작하는 문자 횟수
    b = 0 # 시작하는 문자와 다른 문자 횟수
    i = 1 # 인덱스 번호
    while True:
        if len(word) == 0:
            break
        if len(word) == i:
            answer += 1
            break
        if word[0] == word[i]:
            a += 1
            i += 1
        else:
            b += 1
            i += 1
        if a == b:
            answer += 1
            word = word[i:]
            i = 1
            a = 1
            b = 0
    return answer

# print(solution("banana"))
print(solution("abracadabra"))
# print(solution("aaabbaccccabba"))