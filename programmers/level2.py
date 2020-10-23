def solution(brown, yellow):
    answer = []
    size = list()
    total = 0
    
    for i in range(yellow+1):
        if i == 0:
            pass
        elif (yellow % i) == 0:
            size.append(i)

    s = len(size)//2

    for i in range(s):
        size.pop()


    for i in size:
        big = yellow // i
        total = (big+2)*2 + i*2
        if total == brown:
            answer = [big+2, i+2]

    print(answer)

            
        

    return answer
solution(10, 2)
