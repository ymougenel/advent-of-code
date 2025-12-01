import unittest
import main


class main_test(unittest.TestCase):

    def test_input_example_1(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(3, main.solve_part1(data))

    def test_input_1(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(1066, main.solve_part1(data))

    def test_input_example_2(self):
        data = main.read_file("inputs/example1.txt")
        self.assertEqual(6, main.solve_part2(data))

    def test_overflow(self):
        data = [('R', 60)]
        self.assertEqual(1, main.solve_part2(data))

    def test_big_overflow(self):
        data = [('R', 1000)]
        self.assertEqual(10, main.solve_part2(data))

    def test_extend_2(self):
        data = [('L', 50), ('R', 10)]
        self.assertEqual(1, main.solve_part2(data))

    def test_corner_cases(self):
        data = [('L', 50)]
        self.assertEqual(1, main.solve_part2(data))
        data = [('L', 50), ('L', 100)]
        self.assertEqual(2, main.solve_part2(data))
        data = [('L', 50), ('R', 100)]
        self.assertEqual(2, main.solve_part2(data))
        data = [('R', 50)]
        self.assertEqual(1, main.solve_part2(data))
        data = [('L', 50), ('R', 200)]
        self.assertEqual(3, main.solve_part2(data))
        data = [('L', 50), ('L', 200)]
        self.assertEqual(3, main.solve_part2(data))
        data = [('L', 200)]
        self.assertEqual(2, main.solve_part2(data))
        data = [('R', 200)]
        self.assertEqual(2, main.solve_part2(data))
        data = [('L', 150)]
        self.assertEqual(2, main.solve_part2(data))

    def test_input_2(self):
        data = main.read_file("inputs/input.txt")
        self.assertEqual(6223, main.solve_part2(data))


if __name__ == '__main__':
    unittest.main()
