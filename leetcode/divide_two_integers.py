# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647

        result = 0
        dvd, dvs = abs(dividend), abs(divisor)

        while dvd >= dvs:
            inc = dvs
            i = 0

            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return - result

        return result
