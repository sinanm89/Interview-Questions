# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

#     For example, 121 is a palindrome while 123 is not.
#     also -121 is not

class Solution:
    def isPalindrome(self, x: int) -> bool:
        inp_pal = str(x)

        left_i = 0
        right_i = len(inp_pal) - 1

        while left_i < right_i:

            if inp_pal[left_i] == inp_pal[right_i]:

                left_i += 1
                right_i -= 1

            else:
                return False

        return True





print(Solution().isPalindrome(x=121))
print(Solution().isPalindrome(x=-121))
print(Solution().isPalindrome(x=1132111))
print(Solution().isPalindrome(x=11))
print(Solution().isPalindrome(x=2222))
