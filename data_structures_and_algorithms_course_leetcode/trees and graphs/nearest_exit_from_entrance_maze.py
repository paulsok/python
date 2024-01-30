from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        m = len(maze)
        n = len(maze[0])
        queue = [(entrance[0], entrance[1], 0)]
        seen = {(entrance[0], entrance[1])}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, steps = queue.pop(0)
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or row == m - 1 or col == 0 or col == n - 1):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and maze[next_row][next_col] == '.' and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        
        return -1