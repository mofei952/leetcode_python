"""
question:
https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(3)
    print(obj.deleteHead())
    print(obj.deleteHead())
