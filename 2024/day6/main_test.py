import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(41, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(6, main.solve_part2(data))

    def test_input_1(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(4776, main.solve_part1(data))

    # def test_input_2(self):
    #     data = main.read_file("inputs/input.txt")
    #     self.assertEqual(1586, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
