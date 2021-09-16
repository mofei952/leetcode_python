"""
question:
https://leetcode.com/problems/balanced-binary-tree/
"""

from tree.binary_tree import create_tree


class Solution:

    def isBalanced(self, root):
        def balanced(node):
            if node is None:
                return 0
            h1 = balanced(node.left)
            if h1 == -1:
                return -1
            h2 = balanced(node.right)
            if h2 == -1:
                return -1
            if abs(h1 - h2) > 1:
                return -1
            return 1 + max(h1, h2)

        return balanced(root) != -1

    def isBalanced2(self, root):
        """ 更简洁的写法 """

        def balanced(node):
            if node is None:
                return 0
            h1 = balanced(node.left)
            h2 = balanced(node.right)
            if abs(h1 - h2) > 1:
                raise ValueError('not balanced')
            return 1 + max(h1, h2)

        try:
            balanced(root)
        except ValueError:
            return False
        else:
            return True


if __name__ == '__main__':
    # TODO 比较两种解法的执行效率
    print(Solution().isBalanced2(create_tree([1, None, 2, None, 3])))
    print(Solution().isBalanced2(create_tree([3, 9, 20, None, None, 15, 7])))
    print(Solution().isBalanced2(create_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
    print(Solution().isBalanced2(create_tree([])))
