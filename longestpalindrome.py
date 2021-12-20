# Given a string s, return the longest palindromic substring in s.



# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Input: s = "cbbaabad"
# Output: "aba"


# from typing import str
# aabaa

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        palindrome_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palindrome_len:
                    palindrome = s[l:r+1]
                    palindrome_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > pailndrome_len:
                    palindrome = s[l:r+1]
                    palindrome_len = r - l + 1
                l -= 1
                r += 1

        return palindrome

print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbaabad"))
