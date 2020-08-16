N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse = True)
count = 0
result =0
b = 0


for a in range(M):
  if count < K:
    result += A[b]
    count += 1
  else:
    count =0
    result += A[b+1]

print(result)
