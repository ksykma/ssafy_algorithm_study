# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        if i!=j:
            return i
    
    return participant[-1]