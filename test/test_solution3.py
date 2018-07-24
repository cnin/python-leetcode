import sys
import unittest as ut

sys.path.append('..') 
from solutions import Solution3
from linked_list import LinkedList

class TestSolution3(ut.TestCase):
    
    def setUp(self):
        self.s = Solution3()
        self.list_node = LinkedList()
        for i in range(10):
            self.list_node.append(i)

    def test_print_linked_list_from_tail_to_head(self):
        linked_list = self.s.print_list_from_tail_to_head(self.list_node.head)
        self.assertListEqual(linked_list, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_print_linked_list_from_tail_to_head_alter(self):
        linked_list = self.s.print_list_from_tail_to_head_alter(self.list_node.head)
        self.assertListEqual(linked_list, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    ut.main(verbosity=3)
