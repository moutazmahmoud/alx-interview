#!/usr/bin/python3
"""
Coin Change Problem
Find the minimum number of coins needed to make a given total amount.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet the total amount.
    :param coins: List of coin denominations.
    :param total: The total amount to achieve.
    :return: Minimum number of coins or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the DP array with a value greater than the possible minimum
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0

    # Compute the minimum coins for each amount up to the total
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
