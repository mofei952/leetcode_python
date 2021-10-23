"""
question:
https://leetcode.com/problems/count-complete-tree-nodes/
"""
from typing import Optional

import pytest

from commons import func_test
from tree.binary_tree import create_tree, TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [root]
        n = 0
        while queue:
            n += 1
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return n

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        """ 最坏时间复杂度为O(h^2) """
        hl = hr = 0

        node = root
        while node:
            hl += 1
            node = node.left
        node = root
        while node:
            hr += 1
            node = node.right

        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)


@pytest.fixture(scope="module")
def test_data():
    params_list = []
    res_list = []
    # range(5 * 10 ** 3) test1: 1.82s test2:0.10s
    for i in range(5 * 10 ** 4):
        params = (create_tree(range(i)),)
        params_list.append(params)
        res_list.append(Solution().countNodes2(*params))
    return params_list, res_list, 1


def test1(test_data):
    func_test(Solution().countNodes, *test_data)


def test2(test_data):
    func_test(Solution().countNodes2, *test_data)


if __name__ == '__main__':
    assert Solution().countNodes2(create_tree([1, 2, 3, 4, 5, 6])) == 6
    assert Solution().countNodes2(create_tree([])) == 0
    assert Solution().countNodes2(create_tree([1])) == 1
    assert Solution().countNodes2(create_tree([1, 2, 3, 4])) == 4
