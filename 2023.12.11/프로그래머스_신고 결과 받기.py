def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    id_dict = {id:i for i, id in enumerate(id_list)}
    reported_list = [[] for i in range(len(id_list))]
    for i in range(len(report)):
        fr, to = report[i].split() # fr는 신고하는 사람, to는 신고 당하는 사람
        if fr not in reported_list[id_dict[to]]:
            reported_list[id_dict[to]].append(fr)
    for i in range(len(reported_list)):
        if len(reported_list[i]) >= k:
            for j in range(len(reported_list[i])):
                answer[id_dict[reported_list[i][j]]] += 1
    return answer