
from typing import List


class Solution:
    def coinChange(self, arr: List[str]) -> List[str]:
        # The output character array that will have sorted arr
        output = [0 for i in range(len(arr))]

        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(256)]

        # For storing the resulting answer since the
        # string is immutable
        ans = ["" for _ in arr]

        # Store count of each character
        for i in arr:
            count[ord(i)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(256):
            count[i] += count[i-1]

        # Build the output character array
        for i in range(len(arr)):
            output[count[ord(arr[i])]-1] = arr[i]
            count[ord(arr[i])] -= 1

        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(arr)):
            ans[i] = output[i]
        return ans



        # count = [0] * 12
        # out = [0] * len(coins)

        # for coin in coins:
        #     count[coin] += 1

        # for j in range(1, len(count)):
        #     count[j] += count[j-1]

        # # out[0] = min(count)
        # for i in range(len(out)):
        #     print(out)
        #     out[count[coins[i]]-1] = coins[i]
        #     count[coins[i]] -= 1


        # return out

# Driver program to test above function
arr = "geeksforgeeks"
print(Solution().coinChange(arr))
