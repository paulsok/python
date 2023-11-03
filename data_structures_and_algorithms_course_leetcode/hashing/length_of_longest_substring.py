from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def_dict = defaultdict(int)

        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in def_dict:
                i = max(def_dict[s[j]], i)

            ans = max(ans, j - i + 1)
            def_dict[s[j]] = j + 1

        return ans
