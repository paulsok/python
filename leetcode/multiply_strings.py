# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Note: You must not use any built-in BigInteger library
# or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0

        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))

        return str(res1 * res2)
