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

    # @classmethod
    # def create_tree(cls, arr):
    #     if not arr:
    #         return None
    #
    #     val = arr.pop(0)
    #     if val is None:
    #         return None
    #
    #     node = cls(val)
    #     node.left = cls.create_tree(arr)
    #     node.right = cls.create_tree(arr)
    #
    #     return node

    @staticmethod
    def create_tree(arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = [root]

        for i in range(1, len(arr), 2):
            node = queue.pop(0)

            val = arr[i]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)

            if i + 1 >= len(arr):
                continue
            val = arr[i + 1]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

        return root


if __name__ == '__main__':
    tree = TreeNode.create_tree([1, None, 2, 3])
    print(tree)
