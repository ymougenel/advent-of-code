import unittest
import main

class main_test(unittest.TestCase):

    board1 = [[(22, False), (13, False), (17, False), (11, False), (0, False)], [(8, False), (2, False), (23, False), (4, False), (24, False)], [(21, False), (9, False), (14, False), (16, False), (7, False)], [(6, False), (10, False), (3, False), (18, False), (5, False)], [(1, False), (12, False), (20, False), (15, False), (19, False)]]
    board2 = [[(3, False), (15, False), (0, False), (2, False), (22, False)], [(9, False), (18, False), (13, False), (17, False), (5, False)], [(19, False), (8, False), (7, False), (25, False), (23, False)], [(20, False), (11, False), (10, False), (24, False), (4, False)], [(14, False), (21, False), (16, False), (12, False), (6, False)]]
    def test_w
    def test_input_exemple_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(0, 1)

    def test_input_exemple_2(self):
        data = main.read_file_sliding_window("inputs/part2.example")
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
