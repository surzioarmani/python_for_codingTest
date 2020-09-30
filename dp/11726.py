




def solution(n):
    
    dp = [ 0 for _ in range(n+1)]

    for i in range(n+1):
        if ( i < 4):
            dp[i] = i

        else:
            dp[i] = dp[i-1] + (dp[i-2] * 2)
            
    return dp[n]%10007





n = int(input())


print(solution(n))

