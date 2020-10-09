def solution(N):
    answer = []
    em = []
    num = 1
    stay = 0
    j = 0
    em.append(0)
    for i in range(2, 10):
        first = N
        left = []
        
        while first > i:
            left.append(first%i)
            first = first // i
        left.append(first)
        
        
        for j in range(len(left)):
            if left[j] != 0:
                num *= left[j]
        
        if num >= max(em):
            stay = i
        em.append(num)

        num = 1
            
            
    answer.append(stay)
    answer.append(max(em))
                  
    return answer
