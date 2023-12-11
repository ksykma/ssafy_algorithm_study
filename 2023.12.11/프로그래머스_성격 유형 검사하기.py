def solution(survey, choices):
    answer = ''
    score_dict = {'1':3, '2':2, '3':1, '5':1, '6':2, '7':3}
    personality = {'R':0, 'T':1, 'C':2, 'F':3, 'J':4, 'M':5, 'A':6, 'N':7}
    personality_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score_list = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(survey)):
        if choices[i] < 4:
            score_list[personality[survey[i][0]]] += score_dict[str(choices[i])]
        elif choices[i] > 4:
            score_list[personality[survey[i][1]]] += score_dict[str(choices[i])]           
    for i in range(0, 8, 2):
        if score_list[i] > score_list[i+1]:
            answer += personality_list[i]
        elif score_list[i] < score_list[i+1]:
            answer += personality_list[i+1]
        else:
            if personality_list[i] > personality_list[i+1]:
                answer += personality_list[i+1]
            elif personality_list[i] < personality_list[i+1]:
                answer += personality_list[i]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]	))