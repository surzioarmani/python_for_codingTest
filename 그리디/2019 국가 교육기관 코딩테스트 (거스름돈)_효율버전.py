N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse = True)

first = data[n-1]
second = data[n-2]

 # 가장 큰수가 더해지는 횟수 계싼
count = int(M/ (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) *first
result += (M -count) * second

print(result)
