# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        string = str(abs(x))
        reversed = int(string[::-1])

        if reversed > 2147483647:
            return 0

        elif x > 0:
            return reversed

        return -1 * reversed
