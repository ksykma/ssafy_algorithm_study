from collections import Counter

def solution(lottos, win_nums):
    lottos_dict = {'0':6, '1':6, '2':5, '3':4, '4':3, '5':2, '6':1}
    answer = []
    nums = Counter(lottos) & Counter(win_nums)
    zero = lottos.count(0)
    return lottos_dict[str(len(nums)+zero)], lottos_dict[str(len(nums))]