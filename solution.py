def max_experience(levels, experience):
    dp = [[0] * (i+1) for i in range(levels)]
    dp[0][0] = experience[0][0]
    
    for i in range(1, levels):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + experience[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + experience[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + experience[i][j]
    
    return max(dp[levels-1])

levels = 4
experience = [[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
result = max_experience(levels, experience)
print(result)
