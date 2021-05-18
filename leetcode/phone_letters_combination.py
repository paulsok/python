# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_keyboard = {2: 'abc', 3: 'def', 4: 'ghi',
                          5: 'jkl', 6: 'mno', 7: 'pqrs',
                          8: 'tuv', 9: 'wxyz'}

        answer = [''] if digits else []

        for x in digits:
            answer = [i + j for i in answer for j in phone_keyboard[int(x)]]

        return answer
