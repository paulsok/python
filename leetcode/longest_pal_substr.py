# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ''
        s_len = len(s)

        for i in range(s_len):
            for j in range(s_len, i, -1):

                if len(pal) >= (j - i):
                    break

                elif s[i:j] == s[i:j][::-1]:
                    pal = s[i:j]
                    break
        return pal
