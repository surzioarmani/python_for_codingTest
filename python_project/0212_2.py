result = sum([1,2,3,4])
print(result)

result = min([1,2,3,4])
print(result)


#수학 수식이 문자열 형식일 때 
result = eval("(3+5)*10")
print(result)

#두번째 수를 기준으로 정렬할 때
result = sorted([('홍길동',35),('이순신', 75),('아무개',50)], key = lambda x: x[1], reverse = True)
print(result)

data = [('홍길동',35),('이순신', 75),('아무개',50)]
data.sort(key = lambda x: x[1],reverse = True)
print(data)

#데이터를 뽑아 일렬로 나열하는 모든 경우

from itertools import permutations, combinations, product

data = ['A', 'B', 'C']
result = list(permutations(data,3))    #순열
result1 = list(combinations(data,2))   #조합
result2 = list(product(data,repeat=2)) #중복순열
print(result)
print(result1)
print(result2)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2)) #중복조합
print(result)

#힙
import heapq

def heapsort(iterable):
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 최소 힙
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# bisect 이진탐색, 정렬된 배열에서 특정한 원소를 찾아야 할 때

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 4]
x =4

print(bisect_left(a, x))  #정렬된 순서 유지하면서 list a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(bisect_right(a, x)) #정렬된 순서 유지하면서 list a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

def count_by_range(a,left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a= [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))  # 값이 4인 데이터 개수 출력

print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력


# collections 이용해 가장 앞,뒤쪽에 원소를 삽입

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# 등장 횟수 세는 Counter

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))


import math

print(math.factorial(5))
print(math.gcd(21, 14))

        
