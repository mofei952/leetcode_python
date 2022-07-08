"""
question:
https://leetcode.cn/problems/sort-of-stacks-lcci/
"""


class SortedStack:

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        for i in range(len(self._stack)):
            if val > self._stack[i]:
                self._stack.insert(i, val)
                return
        self._stack.append(val)

    def pop(self) -> None:
        if self.isEmpty():
            return None
        self._stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self._stack[-1]

    def isEmpty(self) -> bool:
        return not bool(self._stack)


if __name__ == '__main__':
    obj = SortedStack()
    obj.push(1)
    obj.push(3)
    obj.push(2)

    print(obj.isEmpty())
    print(obj.peek())
    print(obj.pop())
    print()

    print(obj.isEmpty())
    print(obj.peek())
    print(obj.pop())
    print()

    print(obj.isEmpty())
    print(obj.peek())
    print(obj.pop())
    print()

    print(obj.isEmpty())
