"""
question:
https://leetcode.cn/problems/lru-cache-lcci/
"""
from collections import deque, OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
            self.cache.pop(key)
        if len(self.queue) == self.capacity:
            k = self.queue.popleft()
            self.cache.pop(k)
        self.queue.append(key)
        self.cache[key] = value


class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


class DListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DList:
    def __init__(self):
        self.head = DListNode(None, None)
        self.tail = DListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        prev, next = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        next.prev = node
        node.next = next

    def popleft(self):
        node = self.head.next
        self.pop(node)
        return node

    def pop(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def move_to_end(self, node):
        self.pop(node)
        self.append(node)


class LRUCache3:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.dlist = DList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.dlist.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.dlist.move_to_end(node)
            node.value = value
        else:
            if self.size == self.capacity:
                removed_node = self.dlist.popleft()
                self.cache.pop(removed_node.key)
                self.size -= 1
            node = DListNode(key, value)
            self.cache[key] = node
            self.dlist.append(node)
            self.size += 1


if __name__ == '__main__':
    cache = LRUCache3(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.cache)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.cache)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    # cache = LRUCache3(2)
    # cache.put(2, 1)
    # cache.put(2, 2)
    # print(cache.get(2))
    # cache.put(1, 1)
    # cache.put(4, 1)
    # print(cache.cache)
    # print(cache.get(2))
