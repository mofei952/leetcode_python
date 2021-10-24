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


# @pytest.mark.skip
# def test_data_list(start, stop):
#     arr = list(range(start))
#     for i in range(start, stop):
#         tree = create_tree(arr)
#         count = Solution().countNodes2(tree)
#         arr.append(i + 1)
#         yield tree, count
#
#
# @pytest.mark.parametrize("tree,count", test_data_list(0, 5 * 10 ** 3))
# def test1(tree, count):
#     assert Solution().countNodes(tree) == count
#
#
# @pytest.mark.parametrize("tree,count", test_data_list(0, 5 * 10 ** 3))
# def test2(tree, count):
#     assert Solution().countNodes2(tree) == count


def complete_trees_gen(start, stop):
    if start == 0:
        yield None

    root = TreeNode(1)
    queue = [root]
    if start <= 1:
        yield root

    for i in range(2, stop, 2):
        node = queue.pop(0)

        node.left = TreeNode(i)
        queue.append(node.left)
        if start <= i:
            yield root

        if i + 1 >= stop:
            continue

        node.right = TreeNode(i + 1)
        queue.append(node.right)
        if start <= i + 1:
            yield root


@pytest.mark.skip
def test_data_gen(start, stop):
    generator = complete_trees_gen(start, stop)
    for i in range(start, stop):
        tree = next(generator)
        yield tree, i


def test1():
    for tree, count in test_data_gen(0, 5 * 10 ** 4):
        assert Solution().countNodes(tree) == count


def test2():
    for tree, count in test_data_gen(0, 5 * 10 ** 4):
        assert Solution().countNodes2(tree) == count


# count     test1    test2
# 0~5*10^3  1.82s    0.10s
# 0~5*10^4  163.04s  1.54s


if __name__ == '__main__':
    assert Solution().countNodes2(create_tree([1, 2, 3, 4, 5, 6])) == 6
    assert Solution().countNodes2(create_tree([])) == 0
    assert Solution().countNodes2(create_tree([1])) == 1
    assert Solution().countNodes2(create_tree([1, 2, 3, 4])) == 4
