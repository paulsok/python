# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result, stack = 0, [-1]

        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:
                stack.pop()

                if not stack:
                    stack.append(idx)
                else:
                    result = max(result, idx - stack[-1])

        return result
