def nToKGroups(n,k):
    if n<k:
        return 0
    dp=[[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(i,n+1):
            if i==j:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i][j-i]
    return dp[k][n]


n=nToKGroups(1000000,5)
print(n)