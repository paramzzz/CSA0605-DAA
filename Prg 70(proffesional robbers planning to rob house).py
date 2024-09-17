def house_robber_ii(houses):
    
    n = len(houses)

    if n == 1:
        return houses[0]

    if n == 2:
        return max(houses[0], houses[1])

    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + houses[i])

    return max(dp[-1], dp[-2])


houses = [1,2,3,1]
print("Maximum amount of money that can be stolen:", house_robber_ii(houses))
