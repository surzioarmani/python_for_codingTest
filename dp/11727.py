




def solution(n):
    
    dp = [ 0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 3

    for i in range(n+1):
        if ( i < 3):
            pass

        else:
            dp[i] = dp[i-1]+(dp[i-2] * 2)
            
    return dp[n]%10007





n = int(input())


print(solution(n))

