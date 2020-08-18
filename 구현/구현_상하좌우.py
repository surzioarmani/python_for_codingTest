/*
2020.08.18
작성자: 조수아
*/
N = map(int, input())
x=1
y=1


A = list(map(str, input().split()))

for buf in A:
    if buf == 'R':
        if y == N:
            continue
        else:
            y += 1
            
    elif buf == 'L':
        if y == 1:
            continue
        else:
            y -= 1
        
    elif buf == 'U':
        if x == 1:
            continue
        else:
            x -= 1
        
    elif buf == 'D':
        if x == N:
            continue
        else:
            x += 1

print(x, y)

