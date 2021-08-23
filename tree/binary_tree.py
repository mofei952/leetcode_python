import warnings
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val!r})'

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return str(self) == str(other)

    def depth(self):
        if self is None:
            return 0
        return max(TreeNode.depth(self.left), TreeNode.depth(self.right)) + 1

    def preorder_traversal(self):
        def preorder(root):
            if root is None:
                return []
            return [root.val] + preorder(root.left) + preorder(root.right)

        print(*preorder(self), sep=' ')

    def inorder_traversal(self):
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        print(*inorder(self), sep=' ')

    def postorder_traversal(self):
        def postorder(root):
            if root is None:
                return []
            return postorder(root.left) + postorder(root.right) + [root.val]

        print(*postorder(self), sep=' ')

    def level_traversal(root):
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            print(node.val, end=' ')
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        print()

    def _max_val_length(self):
        if not self:
            return 0
        return max(len(str(self.val)), TreeNode._max_val_length(self.left), TreeNode._max_val_length(self.right))

    def display(self):
        # 树的深度
        depth = self.depth()
        # val长度最大值+2（左右括号）
        length = self._max_val_length() + 2
        # 最后一层节点数量
        last_level_node_count = 2 ** (depth - 1)
        # 整个输出的宽度，即最后一层宽度
        width = last_level_node_count * length + (last_level_node_count - 1) * (length - 2)

        level = 1
        nodes = [self]
        while nodes:
            new_nodes = []
            has_node = False

            datas = []
            for node in nodes:
                text = str(node.val) if node else ''
                if node:
                    if node.left or node.right:
                        has_node = True
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                else:
                    new_nodes.append(None)
                    new_nodes.append(None)
                datas.append(f'({text.center(length - 2, " ")})')

            # 本层节点之间空格数量
            # space_count = 2 ** (depth - level) * length + (2 ** (depth - level) - 1) * (length - 2) - 2
            space_count = 2 ** (depth - level) * (2 * length - 2) - length
            # 下一层节点之间空格数量
            next_space_count = 2 ** (depth - level - 1) * (2 * length - 2) - length
            # 本层每组下划线数量
            underline_count = max(0, (next_space_count - length) // 2)

            # 打印节点行
            print((' ' * space_count).join(datas).center(width))
            # 打印线
            #  ____/    \____
            # /              \
            if level < depth:
                horiz_line = '_' * underline_count
                print(
                    (' ' * (space_count - 2 * underline_count)).join(
                        [horiz_line + '/' + ' ' * (length - 2) + '\\' + horiz_line] * len(datas)
                    ).center(width)
                )
            if level < depth - 1:
                print(
                    (' ' * (next_space_count + 2 * (length - 1))).join(
                        ['/' + ' ' * next_space_count + '\\'] * len(datas)
                    ).center(width)
                )

            # 下一层没有节点则结束
            if has_node is False:
                break

            nodes = new_nodes
            level += 1

    def display2(self):
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

        col_count = 2 ** level - 1
        for i in range(level):
            s = (' ' * (2 ** (level - i) - 1)).join(str(node.val) if node else 'N' for node in level_to_nodes_dict[i])
            print(s.center(col_count))
            if i != level - 1:
                for j in range(2 ** (level - i - 2)):
                    a = '/' + ' ' * (2 * j + 1) + '\\'
                    b = (' ' * (2 ** (level - i) - 3 - 2 * j)).join([a] * (2 ** i))
                    print(b.center(col_count))


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


def create_tree2(arr):
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
    root = TreeNode(arr[0])
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


def create_tree3(arr):
    """
    根据先序构造二叉树
    """
    if not arr:
        return None

    val = arr.pop(0)
    if val is None:
        return None

    node = TreeNode(val)
    node.left = create_tree3(arr)
    node.right = create_tree3(arr)

    return node


def is_same_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)


if __name__ == '__main__':
    # 构造函数测试
    # create_tree([1, None, 2, 3]).display()
    # create_tree([1, 2, 3, None, 4, 5, 6, 7, None]).display()
    # create_tree([1, None, 2, 2, 32, 31, 3, 23, 1, 23, 123, 12, 3, 12, 31, 23, 2]).display()
    #
    # create_tree2([1, None, 2, None, None, None, 3]).display()
    #
    # create_tree3([1, 2, 3, None, None, 4, None, None, 5, None, 6]).display()

    # 用同一个数组比较两种构造方式
    # arr = [1, 2, 3, None, 4, 5, 6, None, None, 7]
    # create_tree(arr).display()
    # create_tree2(arr).display()

    tree = create_tree([1, 2, 3, None, 4, 5, 6, 7, None])
    tree.preorder_traversal()
    tree.inorder_traversal()
    tree.postorder_traversal()
    tree.level_traversal()
    tree.display()
    tree.display2()

    tree = create_tree([1, None, 2, 2, 32, 31, 3, 23, 1, 2311, 12, 12, 3, 12, 31, 23, 2])
    tree.display()
