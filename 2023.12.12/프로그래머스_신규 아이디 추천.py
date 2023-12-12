def solution(new_id):
    answer = ''
    id_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']
    new_id = new_id.lower()
    for i in new_id:
        if i in id_list:
            answer += i
    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution(	"abcdefghijklmn.p"))
print(solution("a...a"))