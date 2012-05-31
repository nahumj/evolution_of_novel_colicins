import unittest

import mutate

class TestShiftByOne(unittest.TestCase):

    def test_shift_by_one(self):
        for _ in range(10):
            x = mutate.shift_by_one(0)
            self.assertIn(x, [-1,1])
