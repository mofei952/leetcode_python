import warnings
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        level_to_nodes_dict = defaultdict(list)
        nodes = [self]
        next_nodes = []
        level = 0
        has_node = True
        while has_node:
            has_node = False
            for node in nodes:
                level_to_nodes_dict[level].append(node)
                if not node:
                    next_nodes.append(None)
                    next_nodes.append(None)
                else:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
                    if node.left or node.right:
                        has_node = True
            level += 1
            nodes = next_nodes
            next_nodes = []

        res = []
        col_count = 2 ** (level) - 1
        for i in range(level):
            s = (' ' * (2 ** (level - i) - 1)).join(str(node.val) if node else 'N' for node in level_to_nodes_dict[i])
            res.append(s.center(col_count))
            if i != level - 1:
                for j in range(2 ** (level - i - 2)):
                    a = '/' + ' ' * (2 * j + 1) + '\\'
                    b = (' ' * (2 ** (level - i) - 3 - 2 * j)).join([a] * (2 ** i))
                    res.append(b.center(col_count))

        return '\n'.join(res)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return str(self) == str(other)

    @staticmethod
    def create_tree(arr):
        """
        根据层序构造二叉树（忽略空节点的子节点）

        examples:
            >> TreeNode.create_tree([1, 2, 3, None, 4, 5, 6, None, None, 7])
                   1
                  / \
                 /   \
                /     \
               /       \
               2       3
              / \     / \
             /   \   /   \
             N   4   5   6
            / \ / \ / \ / \
            N N N N 7 N N N
        """

        if not arr:
            return None

        length = len(arr)
        root = TreeNode(arr[0])
        queue = [root]

        for i in range(1, length, 2):
            node = queue.pop(0)

            val = arr[i]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)

            if i + 1 >= length:
                continue
            val = arr[i + 1]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root

    @classmethod
    def create_tree2(cls, arr):
        """
        根据层序生成二叉树（不省略空节点的子节点）

        Examples:
            >> TreeNode.create_tree2([1, 2, 3, None, 4, 5, 6, None, None, 7])
                   1
                  / \
                 /   \
                /     \
               /       \
               2       3
              / \     / \
             /   \   /   \
             N   4   5   6
            / \ / \ / \ / \
            N N 7 N N N N N
        """

        length = len(arr)
        root = cls(arr[0])
        queue = [root]

        for i in range(1, length, 2):
            node = queue.pop(0)

            if node is not None:
                if arr[i]:
                    node.left = TreeNode(arr[i])
                if i + 1 < length and arr[i + 1]:
                    node.right = TreeNode(arr[i + 1])

                queue.extend((node.left, node.right))
            else:
                queue.extend((None, None))

        return root

    @classmethod
    def create_tree3(cls, arr):
        """
        根据先序构造二叉树
        """
        if not arr:
            return None

        val = arr.pop(0)
        if val is None:
            return None

        node = cls(val)
        node.left = cls.create_tree3(arr)
        node.right = cls.create_tree3(arr)

        return node


if __name__ == '__main__':
    # print(TreeNode.create_tree([1, None, 2, 3]))
    # print(TreeNode.create_tree([1, 2, 3, None, 4, 5, 6, 7, None]))
    # print(TreeNode.create_tree([1, None, 2, 2, 32, 31, 3, 23, 1, 23, 123, 12, 3, 12, 31, 23, 2]))
    #
    # print(TreeNode.create_tree2([1, None, 2, None, None, None, 3]))
    #
    # print(TreeNode.create_tree3([1, 2, 3, None, None, 4, None, None, 5, None, 6]))

    # 用同一个数组比较两种构造方式
    arr = [1, 2, 3, None, 4, 5, 6, None, None, 7]
    print(TreeNode.create_tree(arr))
    print(TreeNode.create_tree2(arr))
