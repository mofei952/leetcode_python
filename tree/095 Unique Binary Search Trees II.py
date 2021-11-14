"""
question:
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
from typing import List, Optional

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def generate(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end + 1):
                ltrees = generate(start, i - 1)
                rtrees = generate(i + 1, end)
                for ltree in ltrees:
                    for rtree in rtrees:
                        node = TreeNode(i)
                        node.left = ltree
                        node.right = rtree
                        trees.append(node)
            return trees

        return generate(1, n)


if __name__ == '__main__':
    assert Solution().generateTrees(3) == [
        create_tree([1, None, 2, None, 3]),
        create_tree([1, None, 3, 2]),
        create_tree([2, 1, 3]),
        create_tree([3, 1, None, None, 2]),
        create_tree([3, 2, None, 1])
    ]
    assert Solution().generateTrees(1) == [create_tree([1])]
    assert Solution().generateTrees(0) == []
