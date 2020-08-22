<<<<<<< HEAD

# 2020.08.19 작성자: 조수아


N, K = map(int, input().split())
result = 0

while N != 1:
    if N >= K & N % K == 0:
         N = N // K
         result += 1

        
    else:
         N = N - 1
         result += 1

         


print(result)
    
    
=======

# 2020.08.19 작성자: 조수아


N, K = map(int, input().split())
result = 0

while N != 1:
    if N >= K & N % K == 0:
         N = N // K
         result += 1

        
    else:
         N = N - 1
         result += 1

         


print(result)
    
    
>>>>>>> 5ca76d22337ab9895a85cd2a769d498a09968ef0
