import sys
import unittest as ut
sys.path.append('.')
sys.path.append('..') 
from solutions import Solution1

class TestSolution1(ut.TestCase):
    
    def setUp(self):
        self.array = [[1,3,4,5],[5,6,10,11],[6,8,11,12],[9,10,14,15]]
        self.s = Solution1()

    def test_find_false(self):
        target = 7
        self.assertEqual(self.s.find(target, self.array), False)

    def test_find_true(self):
        target = 9
        self.assertTrue(self.s.find(target, self.array))
    
    def test_find_false_alter(self):
        target = 7
        self.assertEqual(self.s.find_alter(target, self.array), False)

    def test_find_true_alter(self):
        target = 9
        self.assertTrue(self.s.find_alter(target, self.array))

    
if __name__ == '__main__':
    ut.main(verbosity=3)
