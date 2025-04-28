from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass


# Definition for a binary tree node.
@dataclass
class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right = right

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        min_col, max_col = 0, 0
        columns = defaultdict(list)
        q = deque([(0, root)])
        while q:
            col, node = q.popleft()
            columns[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((col-1, node.left))
            if node.right:
                q.append((col+1, node.right))

        result = []
        for col in range(min_col, max_col+1):
            result.append(columns[col])

        return result


def test_vertical_order():
    s = Solution()
    for case, expected in [
            (TreeNode(val=1), [[1]]),
            (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), [[2],[1],[3]]),
            (TreeNode(val=1, left=TreeNode(val=2)), [[2], [1]]),
            (TreeNode(val=1, right=TreeNode(val=3)), [[1], [3]]),
            (TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3)), right=TreeNode(val=4)), [[3], [2], [1], [4]]),
            (TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=3)), right=TreeNode(val=4)), [[2], [1,3], [4]]),
            (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3, left=TreeNode(val=4))), [[2], [1,4], [3]]),
            (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3, right=TreeNode(val=4))), [[2], [1], [3], [4]]),

    ]:
        assert s.verticalOrder(case) == expected, f"{case=} {expected=}"
    print("Tests passed")

test_vertical_order()
