# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num = ''

        roman_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
                      "C": 100, "XC": 90, "L": 50, "XL": 40,
                      "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        values = roman_dict.values()
        keys = roman_dict.keys()

        i = 0
        while num > 0:
            for _ in range(num // values[i]):
                roman_num += keys[i]
                num -= values[i]
            i += 1

        return roman_num
