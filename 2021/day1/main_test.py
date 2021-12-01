import unittest
import main


class main_test(unittest.TestCase):

    def test_input_exemple_1(self):
        data = main.read_file("inputs/part1.example")
        self.assertEqual(7, main.find_depth_increases(data))

    def test_input_exemple_2(self):
        data = main.read_file_sliding_window("inputs/part2.example")
        self.assertEqual(5, main.find_depth_increases(main.regroup_values(data)))

if __name__ == '__main__':
    unittest.main()
