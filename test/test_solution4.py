import sys
import unittest as ut

sys.path.append('.') 
sys.path.append('..') 
from solutions import Solution4
from impl import TreeNode

class TestSolution4(ut.TestCase):

    def setUp(self):
        """
                    1
            2              5
        3       4       6       7

        pre-order:   1 2 3 4 5 6 7
        in-order:    3 2 4 1 6 5 7
        post-order:  4 2 3 7 6 5 1
        lever-order: 1 2 5 3 4 6 7   

        """
        self.s = Solution4()
        self.pre_ = [1,2,3,4,5,6,7]
        self.in_  = [3,2,4,1,6,5,7]

    def test_reconstruct_binary_tree(self):
        root=self.s.reconstruct_binary_tree(self.pre_, self.in_)
        self.assertEqual(TreeNode.level_traversal(root),[1,2,5,3,4,6,7])


if __name__ == '__main__':
    ut.main(verbosity=3)
