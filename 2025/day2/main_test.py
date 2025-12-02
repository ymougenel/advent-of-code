import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(1227775554, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(4174379265, main.solve_part2(data))

    def test_is_valid(self):
        self.assertEqual(True, main.is_valid(112))
        self.assertEqual(True, main.is_valid(101))
        self.assertEqual(False, main.is_valid(11))
        self.assertEqual(False, main.is_valid(1010))
        self.assertEqual(True, main.is_valid(1188511880))
        self.assertEqual(False, main.is_valid(1188511885))

    def test_is_valid_part2(self):
        self.assertEqual(True, main.is_valid(112, False))
        self.assertEqual(True, main.is_valid(101, False))
        self.assertEqual(False, main.is_valid(111, False))
        self.assertEqual(False, main.is_valid(11, False))
        self.assertEqual(False, main.is_valid(1010, False))
        self.assertEqual(False, main.is_valid(824824824, False))
        self.assertEqual(False, main.is_valid(1188511885, False))

    def test_input_1(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(23701357374, main.solve_part1(data))

    def test_input_2(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(34284458938, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
