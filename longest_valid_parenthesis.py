
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



# Example 1:

# Input: s = "(()"
# out: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:

# Input: s = ")()())"
# out: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:

# Input: s = ""
# out: 0



# Constraints:

#     0 <= s.length <= 3 * 104
#     s[i] is '(', or ')'.



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        out_len = []

        def backtrack(_inp, _open=0, max_len=0):

            for i in range(len(_inp)):
                c = _inp[i]

                if c == '(':
                    ret = backtrack(_inp[i+1:], _open + 1, max_len)

                    if ret:
                        _open += 1
                    else:
                        out_len.append(max_len)
                        max_len = 0
                        _open = 0

                elif c == ')' and _open > 0:
                    if i == len(_inp) - 1:
                        _open -= 1
                        max_len += 1
                        out_len.append(max_len)
                        continue
                    ret = backtrack(_inp[i+1:], _open - 1, max_len + 1)
                    if ret:
                        _open -= 1
                        max_len += 1
                    else:
                        out_len.append(max_len)
                        max_len = 0
                else:
                    out_len.append(max_len)
                    max_len = 0
                    _open = 0

            if _open == 0:
                out_len.append(max_len)
                return True

            return False

        ff = backtrack(s)
        # print(out_len)
        if ff and len(out_len) > 0 :
            # print(out_len)

            return max(out_len) * 2
        return 0

print(Solution().longestValidParentheses('()((()()')) #4

print(Solution().longestValidParentheses("(()()")) #4
print(Solution().longestValidParentheses("(()")) # 2
print(Solution().longestValidParentheses('()()()()()')) #10
print(Solution().longestValidParentheses(")()()())()()")) #6
print(Solution().longestValidParentheses('"()(()"')) # 4
print(Solution().longestValidParentheses('))))()))))')) # 2
print(Solution().longestValidParentheses('((((()(((((')) # 2

# Solution().longestValidParentheses('')

