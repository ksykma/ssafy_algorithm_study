def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
    print(reserve)
    print(reserve[:])
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)

print(solution(5, [2, 4], [1, 3, 5]))