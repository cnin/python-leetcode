# Schlumberger Private
# Copyright (c) 2017 Schlumberger

import os
import sys

from unittest import TestLoader, TextTestRunner

sys.path.append('.')
sys.path.append('..') 

if __name__ == '__main__':

    runner = TextTestRunner(verbosity=2)

    test_dir = os.path.dirname(__file__)
    test_loader = TestLoader()
    suite = test_loader.discover(test_dir, pattern="test_*.py")
    test_results = runner.run(suite)

    if len(test_results.failures ) > 0 :
        print('exit code:', 1)
        sys.exit(1)
    else:
        print('exit code:', 0)
        sys.exit(0)