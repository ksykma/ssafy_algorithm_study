import json
from pprint import pprint

# 배급한 영화가 많은 순으로 배급사 정렬하기
def distributor(movies):
    id_list = []
    for movie in movies:
        id = movie.get('id')
        id_list.append(id)
    
    company_list = []
    for i in range(len(id_list)):
        movie = open(f'data/movies/{id_list[i]}.json', encoding='utf-8')
        movie1 = json.load(movie)
        companys = movie1.get('production_companies')
        for j in range(len(companys)):
            company_list.append(companys[j].get('name'))
    result = []
    for company in company_list:
        cnt_company = company_list.count(company)
        if (company, cnt_company) not in result:
            result.append((company, cnt_company))
    result.sort(key=lambda x:x[1], reverse=True)
    return result
        

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    pprint(distributor(movies_list))