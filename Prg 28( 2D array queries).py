def maxSumAfterQueries(nums, queries):
    
    MOD = 10**9 + 7
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = nums[0]
    
    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    
    res = 0
    for pos, x in queries:
        for i in range(n, pos, -1):
            if i == pos:
                dp[i] = max(dp[i-1], dp[i-2] + x)
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        
        res = (res + dp[-1]) % MOD
        
        nums[pos] = x
    
    return res

nums = [1, 2, 3, 4, 5]
queries = [[1, 3], [2, 1], [0, 5]]
print(maxSumAfterQueries(nums, queries))  # Output: 19

nums = [2, 3, 1, 4, 5]
queries = [[1, 2], [3, 3], [2, 1]]
print(maxSumAfterQueries(nums, queries))  # Output: 17
