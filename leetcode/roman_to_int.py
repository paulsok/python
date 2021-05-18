# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
                      "C": 100, "XC": 90, "L": 50, "XL": 40,
                      "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        n = len(s)
        num = roman_dict[s[n - 1]]

        for i in range(n - 2, -1, -1):
            if roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                num += roman_dict[s[i]]
            else:
                num -= roman_dict[s[i]]

        return num
