def solution(s):
    lst = list(s)
    cnt = 0
    zero = 0
    while lst != ["1"]:
        zero += lst.count("0")
        lst = list(bin(lst.count("1"))[2:])
        cnt += 1    
    return [cnt, zero]

print(solution("110010101001"))