from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer_1, answer_2 = [], []
        winners, loosers = set(), defaultdict(int)

        for match in matches:
            winners.add(match[0])
            loosers[match[1]] += 1

        for winner in winners:
            if not loosers[winner]:
                answer_1.append(winner)

        for loser in loosers:
            if loosers[loser] == 1:
                answer_2.append(loser)

        return [sorted(answer_1), sorted(answer_2)]
