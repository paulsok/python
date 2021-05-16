# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in,
# the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-231, 231 - 1], the final result is 42.

import re


class Solution:
    def myAtoi(self, s):
        match = re.compile(r'^ *([-\+]?\d+)').match(s)

        if not match:
            return 0

        else:
            num = int(match.group(1))

            if num >= 0:
                return min(num, 2 ** 31 - 1)

            elif num < 0:
                return max(num, -2 ** 31)
