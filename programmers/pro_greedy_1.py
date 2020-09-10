def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if not lost:
            break
        elif i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    print(set_lost, set_reserve)

    answer = n - len(set_lost)
    print(answer)
            
    return answer


solution(5,[2,4],[1,3,5])
solution(5,[2,4],[3])
solution(3,[3],[1])
solution(7,[2,3,4],[1,2,3,6])
