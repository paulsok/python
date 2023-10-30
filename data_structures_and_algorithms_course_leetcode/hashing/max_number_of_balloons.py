from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        text_dict = defaultdict(int)

        for letter in text:
            if letter in balloon.keys():
                text_dict[letter] += 1

        ans = 0
        while all(text_dict.values()) > 0:
            for key, value in balloon.items():
                if text_dict[key] >= value:
                    text_dict[key] -= value
                else:
                    return ans
            ans += 1

        return ans

        # x = collections.Counter(text)
        # return min(x['b'], x['a'], x['l']//2, x['o']//2, x['n'])
