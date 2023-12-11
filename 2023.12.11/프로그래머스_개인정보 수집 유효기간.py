def solution(today, terms, privacies):
    answer = []
    terms_dict = {term.split()[0]:int(term.split()[1]) for term in terms }
    year, month, day = map(int, today.split("."))
    today_value = year * 12 * 28 + month * 28 + day
    for i in range(len(privacies)):
        date, check = privacies[i].split()
        b_year, b_month, b_day = map(int, date.split("."))
        date_value = b_year * 12 * 28 + b_month * 28 + b_day + terms_dict[check] * 28 - 1
        if today_value > date_value:
            answer.append(i+1)
    return answer

# def solution(today, terms, privacies):
#     answer = []
#     terms_dict = {term.split()[0]:int(term.split()[1]) for term in terms }
#     year, month, day = map(int, today.split("."))
#     for i in range(len(privacies)):
#         date, check = privacies[i].split()
#         b_year, b_month, b_day = map(int, date.split("."))
#         if b_month + terms_dict[check] > 12:
#             b_year += (b_month + terms_dict[check]) // 12
#             b_month = b_month + terms_dict[check] - ((b_month + terms_dict[check]) // 12) * 12
#             if b_month == 0:
#                 b_year -= 1
#                 b_month = 12
#             if b_day == 1:
#                 if b_month == 1:
#                     b_year -= 1
#                     b_month = 12
#                     b_day = 28
#                 else:
#                     b_month -= 1
#                     b_day = 28
#             else:
#                 b_day -= 1
#         else:
#             b_month += terms_dict[check]
#             if b_day == 1:
#                 if b_month == 1:
#                     b_year -= 1
#                     b_month = 12
#                     b_day = 28
#                 else:
#                     b_month -= 1
#                     b_day = 28
#             else:
#                 b_day -= 1
#         if year > b_year:
#             answer.append(i+1)
#         elif year == b_year:
#             if month > b_month:
#                 answer.append(i+1)
#             elif month == b_month:
#                 if day > b_day:
#                     answer.append(i+1)
        
#     return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2009.12.31", ["A 13"], ["2008.11.03 A"]))