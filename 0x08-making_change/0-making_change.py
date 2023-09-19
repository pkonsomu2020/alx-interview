#!/usr/bin/python3
"""given a pile of coins of different values determine the fewest coins"""

def makeChange(coins, total):
    # Create a list to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make a total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp for each total amount from coin value to the target total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if it's possible to make the target total
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1