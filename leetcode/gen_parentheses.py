# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                answer.append("".join(S))

            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()

            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()

        backtrack()
        return answer
