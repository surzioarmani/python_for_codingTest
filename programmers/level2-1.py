def solution(bridge_length, weight, truck_weights):
    answer = 0
    first = 0
    t = 0
    line=[0,0]
    warn = 0
    w = truck_weights
    for i in range(len(w)):
     
        if warn == 0:
            if i == 0 :
                first = w[i]
                t += 1
            elif w[i]+first <= weight:
                t+= 1
                first = w[i]
            elif w[i]+first > weight:
                t+= 2
                warn = 1
        elif warn ==1:
            first = w[i-1]
            warn = 0
            if i == 0 :
                first = w[i]
                t += 1
            elif w[i]+first <= weight:
                t+= 1
                first = w[i]
            elif w[i]+first > weight:
                t+= 2
                warn = 1

    
    if warn == 1:
        t+=2
    else:
         t+=1
    print(t)
            
    return answer

solution(2, 10, [7,4,5,6])
solution(100, 100, [10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
