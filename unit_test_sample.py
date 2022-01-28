import unittest

from some_function import multiply_with_loop_bad_function, multiply_with_loop_better_function

class TestCaseBad(unittest.TestCase):
    def test_with_two_positive(self):
        self.assertEqual(multiply_with_loop_bad_function(3,8), 3*8)
        self.assertEqual(multiply_with_loop_bad_function(13,29), 13*29)
        self.assertEqual(multiply_with_loop_bad_function(139,229), 139*229)
        self.assertEqual(multiply_with_loop_bad_function(1397,2297), 1397*2297)
        self.assertEqual(multiply_with_loop_bad_function(1,2), 2)
        # self.assertEqual(multiply_with_loop_bad_function(0.0023131,0.000013233), 0.0023131 * 0.000013233)

    def test_with_one_zero(self):
        self.assertEqual(multiply_with_loop_bad_function(0,8), 0)
        self.assertEqual(multiply_with_loop_bad_function(13,0), 0)

    def test_with_two_zero(self):
        self.assertEqual(multiply_with_loop_bad_function(0,0), 0)

    def test_with_one_negative(self):
        self.assertEqual(multiply_with_loop_bad_function(-1,8), -1*8)
        self.assertEqual(multiply_with_loop_bad_function(13,-1), 13*-1)
        self.assertEqual(multiply_with_loop_bad_function(-139,229), -139*229)
        self.assertEqual(multiply_with_loop_bad_function(1397,-2297), 1397*-2297)
        # self.assertEqual(multiply_with_loop_bad_function(0.0023131,-0.000013233), 0.0023131 * -0.000013233)
        # self.assertEqual(multiply_with_loop_bad_function(-0.0023131,0.000013233), -0.0023131 * 0.000013233)

    def test_with_two_negative(self):
        self.assertEqual(multiply_with_loop_bad_function(-1,-8), -1*-8)
        self.assertEqual(multiply_with_loop_bad_function(-13,-1), -13*-1)
        self.assertEqual(multiply_with_loop_bad_function(-139,-229), -139*-229)
        self.assertEqual(multiply_with_loop_bad_function(-1397,-2297), -1397*-2297)
        # self.assertEqual(multiply_with_loop_bad_function(-0.0023131,-0.000013233), -0.0023131 * -0.000013233)
        # self.assertEqual(multiply_with_loop_bad_function(-0.0023131,-0.000013233), -0.0023131 * -0.000013233)

class TestCase(unittest.TestCase):
    def test_with_two_positive(self):
        self.assertEqual(multiply_with_loop_better_function(3,8), 3*8)
        self.assertEqual(multiply_with_loop_better_function(13,29), 13*29)
        self.assertEqual(multiply_with_loop_better_function(139,229), 139*229)
        self.assertEqual(multiply_with_loop_better_function(1397,2297), 1397*2297)
        self.assertEqual(multiply_with_loop_better_function(1,2), 2)
        # self.assertEqual(multiply_with_loop_better_function(0.0023131,0.000013233), 0.0023131 * 0.000013233)

    def test_with_one_zero(self):
        self.assertEqual(multiply_with_loop_better_function(0,8), 0)
        self.assertEqual(multiply_with_loop_better_function(13,0), 0)

    def test_with_two_zero(self):
        self.assertEqual(multiply_with_loop_better_function(0,0), 0)

    def test_with_one_negative(self):
        self.assertEqual(multiply_with_loop_better_function(-1,8), -1*8)
        self.assertEqual(multiply_with_loop_better_function(13,-1), 13*-1)
        self.assertEqual(multiply_with_loop_better_function(-139,229), -139*229)
        self.assertEqual(multiply_with_loop_better_function(1397,-2297), 1397*-2297)
        # self.assertEqual(multiply_with_loop_better_function(0.0023131,-0.000013233), 0.0023131 * -0.000013233)
        # self.assertEqual(multiply_with_loop_better_function(-0.0023131,0.000013233), -0.0023131 * 0.000013233)

    def test_with_two_negative(self):
        self.assertEqual(multiply_with_loop_better_function(-1,-8), -1*-8)
        self.assertEqual(multiply_with_loop_better_function(-13,-1), -13*-1)
        self.assertEqual(multiply_with_loop_better_function(-139,-229), -139*-229)
        self.assertEqual(multiply_with_loop_better_function(-1397,-2297), -1397*-2297)
        # self.assertEqual(multiply_with_loop_better_function(-0.0023131,-0.000013233), -0.0023131 * -0.000013233)
        # self.assertEqual(multiply_with_loop_better_function(-0.0023131,-0.000013233), -0.0023131 * -0.000013233)
        
