from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)  # or Counter()
        for letter in magazine:
            mag[letter] += 1

        for letter in ransomNote:
            if mag[letter] <= 0:
                return False
            mag[letter] -= 1

        return True
