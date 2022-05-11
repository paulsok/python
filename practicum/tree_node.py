class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_layered_representation(root):
    result = []
    DFS(root, 0, result)
    return result


def DFS(node, depth, result):
    if not node:
        return
    # Т.к. мы выбрали preorder, то результат нужно увеличивать
    # не больше, чем на 1
    if depth >= len(result):
        result.append([])
    result[depth].append(node.val)
    DFS(node.left, depth + 1, result)
    DFS(node.right, depth + 1, result)
