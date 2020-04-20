import unittest

from utility.color_bars import parse_set_string, join_set_string


class TestSetString(unittest.TestCase):
    def test_set_string_00(self):
        self.assertEqual(([1, 2, 3], [4, 5, 6, 7, 8]), parse_set_string('1_2_3__4_5_6_7_8'))

    def test_set_string_01(self):
        self.assertEqual(([1, 2, 3, 4, 5, 6, 7, 8], []), parse_set_string('1_2_3_4_5_6_7_8__'))

    def test_set_string_02(self):
        self.assertEqual(([], [1, 2, 3, 4, 5, 6, 7, 8]), parse_set_string('__1_2_3_4_5_6_7_8'))

    def test_set_string_03(self):
        self.assertEqual('1_2_3__4_5_6_7_8', join_set_string([1, 2, 3], [4, 5, 6, 7, 8]))

    def test_set_string_04(self):
        self.assertEqual('1_2_3_4_5_6_7_8__', join_set_string([1, 2, 3, 4, 5, 6, 7, 8], []))

    def test_set_string_05(self):
        self.assertEqual('__1_2_3_4_5_6_7_8', join_set_string([], [1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    unittest.main()
