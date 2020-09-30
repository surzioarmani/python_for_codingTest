



def solution(n):
    
    dp = [0,1,2,4]
    
    for i in range(n+1):
        if (i > 3):
            a = (dp[i-1] + dp[i-2] + dp[i-3])
            dp.append(a)

    return dp[n]



ans = list()
n = int(input())

for i in range(n):
    ans.append(solution(int(input())))


for i in range(n):
    print(ans[i])

