class Solution:
    def totalNQueens(self, n):
        def backtrack(row, diagonals, anti_diagonals, cols):
            # Base case - N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = 1 << (row - col + n) # add n to avoid going negative
                curr_anti_diagonal = 1 << (row + col)
                curr_col = 1 << col
                
                # Check if bits are set
                if (cols & curr_col
                   or diagonals & curr_diagonal
                   or anti_diagonals & curr_anti_diagonal):
                    continue

                # "Add" the queen to the board
                cols ^= curr_col
                diagonals ^= curr_diagonal
                anti_diagonals ^= curr_anti_diagonal

                # Move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols ^= curr_col
                diagonals ^= curr_diagonal
                anti_diagonals ^= curr_anti_diagonal

            return solutions

        return backtrack(0, 0, 0, 0)
