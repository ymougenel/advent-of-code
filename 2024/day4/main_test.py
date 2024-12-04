import unittest
import main

class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(18, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example2.txt")
        self.assertEqual(9, main.solve_part2(data))

    def test_input_input(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(1877, main.solve_part2(data))

if __name__ == '__main__':
    unittest.main()
