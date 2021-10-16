"""
question:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
from tree.binary_tree import create_tree, TreeNode


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
    res = Solution().connect(create_tree([1, 2, 3, 4, 5, 6, 7]))
    assert tree_to_list(res) == [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']

    res = Solution().connect(create_tree([]))
    assert tree_to_list(res) == []
