import sys
import unittest as ut
sys.path.append('.')
sys.path.append('..') 
from solutions import Solution2

class TestSolution1(ut.TestCase):
    
    def setUp(self):
        self.s = Solution2()

    def test_replace_space(self):
        str_ = "we are happy"
        self.assertEqual(self.s.replace_space(str_), "we%20are%20happy")
    
if __name__ == '__main__':
    ut.main(verbosity=3)
