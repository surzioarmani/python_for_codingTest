def solution(k, score):
    answer = -1
    an = []
    diff = []
    li = []
    count = []
    check = []
    n_diff = []
    first = 0
    diff_list =[]

    # 차이 넣어주기 
    for i in range(len(score)):
        if i == 0:
            first = score[i]

        elif i != len(score):
            t = first - score[i]
            diff.append(t)
            first = score[i]
            if t not in diff_list:
                diff_list.append(t)

    # 사이즈
    if (len(diff) % 2) == 0:
        size = len(diff) // 2
    elif (len(diff) % 2) == 1:
        size = len(diff) // 2 + 1

    for i in range(len(diff_list)):
        if diff.count(diff_list[i]) >= k:
            check.append(diff_list[i])
    second = -1
    
    for i in range(len(score)):
        if i == 0:
            first = score[i]
            an.append(i)
        elif i != len(score):
            t = first - score[i]
            first = score[i]
            if t in check:
                if second in check:
                    pass
                else:
                    if len(an) == 0:
                        pass                    
                    else:
                        an.pop()
                      
            else:
                an.append(i)               
            second = t

                
    if answer == len(score):
        answer = 0
    else:
        answer = len(an)
    
            
            

    return answer
