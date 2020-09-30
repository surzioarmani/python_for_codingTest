n = int(input())


dp = [0 for _ in range(n+1)]  #dp를 이용할 거기 때문에

for i in range(2, n+1):   # 2부터 시작하여 dp[1]은 이미 0으로 설정되어 있으니까 n+1이라고 해서 n까지라고

    dp[i] = dp[i-1] + 1   #  1을 빼고 최소의 연산개수를 구하는 경우

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:  # 2로 나눠떨어지는데 최소의 연산개수가 더적은경우 
        dp[i] = dp[i//2] + 1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:  # 3으로 나눠떨어지는데 최소의연산개수가 더 적은 경우
        dp[i] = dp[i//3] + 1

print(dp[i])
    
