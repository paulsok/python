# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# naive
# class Solution:
#     def check(s, start, end):
#         chars = [0] * 128
#         for i in range(start, end + 1):
#             c = s[i]
#             chars[ord(c)] += 1
#             if chars[ord(c)] > 1:
#                 return False
#         return True

#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         res = 0

#         for i in range(n):
#             for j in range(i, n):
#                 if check(s, i, j):
#                     res = max(res, j - i + 1)
#         return res


# sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
