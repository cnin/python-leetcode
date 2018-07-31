#coding=utf8
#ref: https://www.cnblogs.com/king-ding/p/pythonchaintable.html

from .list_node import ListNode

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data_or_node):

        item = data_or_node if isinstance(data_or_node, ListNode) else ListNode(data_or_node)

        if not self.head:
            self.head = item

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
