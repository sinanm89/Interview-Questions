
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.



# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0



# Constraints:

#     1 <= coins.length <= 12
#     1 <= coins[i] <= 2**31 - 1
#     0 <= amount <= 104


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        coins.sort(reverse=True)
        min_coins = 0

        def backtrack(_coins, _amount, _min_coins):
            i = 0
            while i < len(coins) - 1:
                coin = _coins[i]
                _min_coins += _amount // coin
                _amount = _amount % coin
                _amount, _min_coins = backtrack(_coins, _amount % coin, _amount // coin)
                if _amount == 0 and _min_coins > 0:
                    return _amount, _min_coins
                i += 1

            return -1, -1


        for i in coins:
            _amount, _min_coins = backtrack(coins, amount, min_coins)
            if _amount == 0:
                return min_coins
        return  -1

# Driver program to test above function
# ans = countSort(arr)
# print("Sorted character array is % s" %("".join(ans)))

coins = [1, 4, 1, 2, 7, 5, 2]
amount = 33
# 5

coins = [186,419,83,408]
amount = 6249
# 20

print(Solution().coinChange(coins, amount))
