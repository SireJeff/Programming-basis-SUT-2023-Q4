def count_ways_to_make_change(amount, coins):
    dp = [0] * (amount + 1)

    for coin in coins:

        for i in range(coin, amount + 1):

            dp[i] += dp[i - coin]
    return dp[amount]