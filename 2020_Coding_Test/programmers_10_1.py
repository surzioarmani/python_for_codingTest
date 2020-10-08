def solution(n):
    answer = 0
    first = n
    left = []
    while first > 3:
        left.append(first % 3)
        first = first // 3
    left.append(first)
    print(left)
    n = 1
    for i in range(len(left)):
        answer += left[len(left)-1-i] * n
        n *= 3
        print(n)
    print(answer)
    return answer
