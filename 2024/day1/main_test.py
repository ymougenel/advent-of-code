import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        l1, l2 = main.read_file("inputs/example1.txt")
        l1.sort()
        l2.sort()
        self.assertEqual(11, main.solve_part1(l1, l2))

    def test_input_part1(self):
        l1, l2 = main.read_file("inputs/input.txt")
        l1.sort()
        l2.sort()
        self.assertEqual(1151792, main.solve_part1(l1, l2))

    def test_input_example_2(self):
        l1,l2 = main.read_file("inputs/example1.txt")
        l1.sort()
        l2.sort()
        self.assertEqual(31, main.solve_part2(l1,l2))


if __name__ == '__main__':
    unittest.main()
