def solution(numbers):
    answer1 = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j and numbers[i]+numbers[j] not in answer1:
                answer1.append(numbers[i]+numbers[j])
            
    answer=list(set(answer1))
 
    print(answer)
    return answer
