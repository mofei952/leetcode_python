#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/12 21:20
# @File    : list_node.py
# @Software: PyCharm


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_linked_list(cls, nums):
        if not nums:
            return None
        root = cls(nums[0])
        temp = root
        for i in nums[1:]:
            temp.next = cls(i)
            temp = temp.next
        return root

    def __str__(self):
        value_list = []
        t = self
        while t:
            value_list.append(str(t.val))
            t = t.next
        return '->'.join(value_list)
