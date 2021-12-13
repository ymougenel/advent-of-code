import unittest
import main

class main_test(unittest.TestCase):

    def test_input_exemple_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(0, 1)

    def test_input_exemple_2(self):
        data = main.read_file_sliding_window("inputs/part2.example")
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()
