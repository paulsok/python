from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def is_valid_mutation(gene1, gene2):
            diff = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        def dfs(gene, steps):
            if gene == endGene:
                self.min_steps = min(self.min_steps, steps)
                return
            
            for i in range(len(bank)):
                if bank[i] not in self.visited and is_valid_mutation(gene, bank[i]):
                    self.visited.add(bank[i])
                    dfs(bank[i], steps + 1)
                    self.visited.remove(bank[i])
        
        self.min_steps = float('inf')
        self.visited = set()
        dfs(startGene, 0)
        return self.min_steps if self.min_steps != float('inf') else -1
