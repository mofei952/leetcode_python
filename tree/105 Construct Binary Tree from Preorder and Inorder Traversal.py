"""
question:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List

import pytest

from commons import func_test
from tree.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        val = preorder[0]
        index = inorder.index(val)
        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return node

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder_index = 0
        inorder_indexes = {v: i for i, v in enumerate(inorder)}

        def recursive(left, right):
            nonlocal preorder_index
            if left == right:
                return None

            val = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(val)

            node.left = recursive(left, inorder_indexes[val])
            node.right = recursive(inorder_indexes[val] + 1, right)

            return node

        tree = recursive(0, len(inorder))
        return tree


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
    ]
    res_list = []
    for params in params_list:
        res_list.append(Solution().buildTree(*params))
    return params_list, res_list, 10000


def test_105(test_data):
    func_test(Solution().buildTree, *test_data)


def test_105_2(test_data):
    func_test(Solution().buildTree2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q',
                 'tree/105 Construct Binary Tree from Preorder and Inorder Traversal.py'])
