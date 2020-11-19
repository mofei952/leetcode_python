from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        col_count = 2**(level)-1
        for i in range(level):
            s = (' ' * (2**(level-i)-1)).join(str(node.val) if node else 'N' for node in level_to_nodes_dict[i])
            res.append(s.center(col_count))
            if i != level-1:
                for j in range(2 ** (level-i-2)):
                    a = '/' + ' ' * (2*j+1) + '\\'
                    b = (' ' * (2 ** (level-i)-3-2*j)).join([a] * (2 ** i))
                    res.append(b.center(col_count))

        return '\n'.join(res)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return str(self) == str(other)

    @staticmethod
    def create_tree(list):
        if not list:
            return None
        root = TreeNode(list[0])
        queue = [root]
        node = None
        for i, val in enumerate(list[1:]):
            if i % 2 == 0:
                node = queue.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
            else:
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root
