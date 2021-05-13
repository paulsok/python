# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1, l2):
        num_1 = int(''.join(map(str, l1[::-1])))
        num_2 = int(''.join(map(str, l2[::-1])))
        return [int(x) for x in str(num_1 + num_2)][::-1]
