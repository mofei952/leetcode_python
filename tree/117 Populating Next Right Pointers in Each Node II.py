"""
quesions:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
from tree.binary_tree import TreeNode, create_tree


def __init__(self, val=0, left=None, right=None, next=None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next


TreeNode.__init__ = __init__


class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        queue = [root]
        while queue:
            new_queue = []
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
            queue[-1].next = None
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return root


def tree_to_list(root):
    if root is None:
        return []
    queue = [root]
    res = []
    while queue:
        node = queue[0]
        while node:
            res.append(node.val)
            node = node.next
        res.append('#')

        new_queue = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue

    return res


if __name__ == '__main__':
    res = Solution().connect(create_tree([1, 2, 3, 4, 5, None, 7]))
    assert tree_to_list(res) == [1, '#', 2, 3, '#', 4, 5, 7, '#']

    res = Solution().connect(create_tree([]))
    assert tree_to_list(res) == []
