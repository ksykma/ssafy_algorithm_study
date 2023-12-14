from collections import Counter

def solution(X, Y):
    nums = Counter(X) & Counter(Y)
    if not nums:
        return '-1'
    elif list(nums) == ['0']:
        return '0'
    nums_order = sorted(list(nums), reverse=True)
    answer = ''
    for num in nums_order:
        answer += num * nums[num]
    return answer

# def solution(X, Y):
#     answer = ''
#     lst = []
#     lst_Y = list(Y)
#     for i in X:
#         if i in lst_Y:
#             lst.append(int(i))
#             lst_Y.remove(i)
#     if len(lst) == 0:
#         return "-1"
#     elif sum(lst) == 0:
#         return "0"
#     else:
#         lst.sort(reverse=True)
#         for i in lst:
#             answer += str(i)
#         return answer

# print(solution("100", "2345"))
# print(solution("100", "203045"))
print(solution("100", "123450"))
# print(solution("12321", "42531"))
# print(solution("5525", "1255"))