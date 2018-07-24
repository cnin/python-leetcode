#encoding=utf8
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""

class Solution3(object):
    def print_list_from_tail_to_head(self, node):
        list_ = []
        head = node
        while head:
            list_.insert(0, head.val)
            head = head.next
        return list_

    def print_list_from_tail_to_head_alter(self, node):
        list_ = []
        head = node
        while head:
            list_.append(head.val)
            head = head.next
        list_.reverse()
        return list_