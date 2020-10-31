def solution(n, delivery):
    answer = ''
    count=[ '?' for i in range(n+1)]
    print(count)

    delivery.sort(reverse=True,key=lambda x:x[2])

    for i in range(len(delivery)):

        if delivery[i][2] == 1:
            count[delivery[i][0]] = 'O'
            count[delivery[i][1]] = 'O'


        elif count[delivery[i][0]] == 'O':
            count[delivery[i][1]] = 'X'


        elif count[delivery[i][1]] == 'O':
            count[delivery[i][0]] = 'X'


    

    for i in range(n):
        answer+=str(count[i+1])

            
            
            
    
    return answer


solution(6,[[1,3,1],[3,5,0],[5,4,0],[2,5,0]])
solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]])
