/*
2020.08.18
작성자: 조수아
*/
N, M = map(int, input().split())

c=9
a=list()
b=list()
for i in range(N):
        a = list(map(int, input().split()))
        a.append(min(a))
        if c >= min(a):
            b.append(min(a))


print(max(b))


