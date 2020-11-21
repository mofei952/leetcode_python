"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

from functools import lru_cache
from typing import List

from tree.tree_node import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        @lru_cache(None)
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left, node.right = left, right
                        trees.append(node)
            return trees or [None]
        return generate(1, n) if n else []


if __name__ == "__main__":
    import time
    t = time.time()
    trees = Solution().generateTrees(15)
    print(time.time() - t)
    # for tree in trees:
    #     print(tree)
